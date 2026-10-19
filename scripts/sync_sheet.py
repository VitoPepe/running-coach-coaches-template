#!/usr/bin/env python3
"""Exporte un classeur Google Sheets publié en .xlsx en un CSV par onglet.

Usage : sync_sheet.py <url ou chemin .xlsx> <dossier de sortie>
Les CSV produits sont générés : ne pas les éditer à la main.
Stdlib uniquement, pour tourner tel quel dans GitHub Actions.
"""
import csv
import datetime as dt
import io
import os
import re
import sys
import unicodedata
import urllib.request
import zipfile
import xml.etree.ElementTree as ET

NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pr": "http://schemas.openxmlformats.org/package/2006/relationships",
}
R_ID = "{%s}id" % NS["r"]
# Formats de date intégrés d'Excel (numFmtId) → rendus en ISO.
BUILTIN_DATE_IDS = set(range(14, 18)) | {22}


def load_bytes(src):
    if os.path.exists(src):
        with open(src, "rb") as f:
            return f.read()
    with urllib.request.urlopen(src, timeout=60) as resp:
        return resp.read()


def slug(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "onglet"


def col_index(ref):
    letters = re.match(r"[A-Z]+", ref).group(0)
    n = 0
    for ch in letters:
        n = n * 26 + ord(ch) - 64
    return n - 1


def text_of(el):
    return "".join(t.text or "" for t in el.iter("{%s}t" % NS["m"]))


def rels(z, path):
    if path not in z.namelist():
        return {}
    root = ET.fromstring(z.read(path))
    return {r.get("Id"): r.get("Target") for r in root.findall("pr:Relationship", NS)}


def date_formats(z):
    """Retourne {index de style: format de date} pour les styles qui affichent une date."""
    root = ET.fromstring(z.read("xl/styles.xml"))
    custom = {
        int(f.get("numFmtId")): f.get("formatCode")
        for f in root.findall("m:numFmts/m:numFmt", NS)
    }
    out = {}
    for i, xf in enumerate(root.findall("m:cellXfs/m:xf", NS)):
        fid = int(xf.get("numFmtId", 0))
        if fid in BUILTIN_DATE_IDS:
            out[i] = "yyyy-mm-dd"
        elif fid in custom:
            code = re.sub(r'"[^"]*"|\[[^\]]*\]', "", custom[fid]).lower()
            if re.search(r"[dmy]", code) and not re.search(r"[0#h]", code):
                out[i] = custom[fid]
    return out


def render_date(serial, fmt):
    # Sheets interprète « 7/10 » comme une date : on restitue le texte affiché.
    d = dt.date(1899, 12, 30) + dt.timedelta(days=int(float(serial)))
    tokens = {"yyyy": f"{d.year:04d}", "yy": f"{d.year % 100:02d}",
              "mm": f"{d.month:02d}", "m": str(d.month),
              "dd": f"{d.day:02d}", "d": str(d.day)}
    return re.sub(r"yyyy|yy|mm|m|dd|d", lambda t: tokens[t.group(0)], fmt.lower())


def render_number(v):
    f = float(v)
    return str(int(f)) if f.is_integer() else v


def read_sheet(z, path, shared, dfmt):
    root = ET.fromstring(z.read(path))
    links = rels(z, path.replace("worksheets/", "worksheets/_rels/") + ".rels")
    hyperlinks = {
        h.get("ref"): links.get(h.get(R_ID))
        for h in root.findall("m:hyperlinks/m:hyperlink", NS)
        if h.get(R_ID) in links
    }
    rows = {}
    for row in root.findall("m:sheetData/m:row", NS):
        r = int(row.get("r")) - 1
        for c in row.findall("m:c", NS):
            ref, t, s = c.get("r"), c.get("t"), int(c.get("s", 0))
            v = c.find("m:v", NS)
            if t == "s" and v is not None:
                val = shared[int(v.text)]
            elif t == "inlineStr":
                val = text_of(c)
            elif t == "b" and v is not None:
                val = "TRUE" if v.text == "1" else "FALSE"
            elif v is not None and v.text is not None:
                val = render_date(v.text, dfmt[s]) if s in dfmt else (
                    v.text if t in ("str", "e") else render_number(v.text))
            else:
                val = ""
            val = val.strip()
            url = hyperlinks.get(ref)
            if url and url != val:
                val = f"{val} ({url})" if val else url
            if val:
                rows.setdefault(r, {})[col_index(ref)] = val
    if not rows:
        return []
    width = max(max(cols) for cols in rows.values()) + 1
    return [[rows.get(r, {}).get(c, "") for c in range(width)] for r in range(max(rows) + 1)]


def export_xlsx(src, out_dir):
    """Écrit un CSV par onglet du classeur `src` (URL ou chemin) dans `out_dir`."""
    data = load_bytes(src)
    if not data.startswith(b"PK"):
        head = data[:200].lstrip().lower()
        got = "une page HTML" if head.startswith((b"<", b"<!doctype")) else "du texte (CSV ?)"
        raise ValueError(
            f"le lien ne renvoie pas un .xlsx mais {got}. Utiliser le lien "
            "« Publier sur le web » au format .xlsx : il doit se terminer par /pub?output=xlsx")
    z = zipfile.ZipFile(io.BytesIO(data))

    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        sst = ET.fromstring(z.read("xl/sharedStrings.xml"))
        shared = [text_of(si) for si in sst.findall("m:si", NS)]
    dfmt = date_formats(z)
    wb_rels = rels(z, "xl/_rels/workbook.xml.rels")
    wb = ET.fromstring(z.read("xl/workbook.xml"))

    os.makedirs(out_dir, exist_ok=True)
    written = set()
    for sh in wb.findall("m:sheets/m:sheet", NS):
        target = wb_rels[sh.get(R_ID)].lstrip("/")
        path = target if target.startswith("xl/") else "xl/" + target
        name = slug(sh.get("name")) + ".csv"
        with open(os.path.join(out_dir, name), "w", newline="", encoding="utf-8") as f:
            csv.writer(f, lineterminator="\n").writerows(read_sheet(z, path, shared, dfmt))
        written.add(name)
        print(f"{sh.get('name')} -> {name}")

    # Onglet supprimé ou renommé dans Sheets → on retire l'ancien CSV.
    for old in os.listdir(out_dir):
        if old.endswith(".csv") and old not in written:
            os.remove(os.path.join(out_dir, old))
            print(f"supprimé : {old}")


def main():
    if len(sys.argv) != 3 or not sys.argv[1]:
        sys.exit("usage : sync_sheet.py <url ou chemin .xlsx> <dossier de sortie>")
    export_xlsx(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
