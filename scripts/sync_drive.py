#!/usr/bin/env python3
"""Synchronise les documents Google Drive listés dans drive-sources/sources.json.

Usage : sync_drive.py [config]   (défaut : drive-sources/sources.json)

Chaque source indique le nom (`secret`) du secret ou de la variable GitHub Actions qui
contient son URL. Ordre de recherche : secrets (DRIVE_SECRETS = toJSON(secrets)), variables
(DRIVE_VARS = toJSON(vars)), puis variable d'environnement du même nom (pratique en local).
Une source sans URL est ignorée avec un avertissement : on peut déclarer une source
avant d'avoir créé son secret.

Types :
- xlsx : classeur Google Sheets (publié en .xlsx) → un CSV par onglet dans `out` (dossier)
- file : document téléchargé tel quel dans `out` (fichier), ex. un Google Doc exporté en .md
Stdlib uniquement, pour tourner tel quel dans GitHub Actions.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sync_sheet import export_xlsx, load_bytes  # noqa: E402


def url_for(name, secrets, variables):
    return (secrets.get(name) or variables.get(name) or os.environ.get(name) or "").strip()


def main():
    config = sys.argv[1] if len(sys.argv) > 1 else "drive-sources/sources.json"
    with open(config, encoding="utf-8") as f:
        sources = json.load(f)["sources"]
    secrets = json.loads(os.environ.get("DRIVE_SECRETS") or "{}")
    variables = json.loads(os.environ.get("DRIVE_VARS") or "{}")

    failed = []
    for src in sources:
        name, kind, out = src["secret"], src["type"], src["out"]
        url = url_for(name, secrets, variables)
        if not url:
            print(f"::warning::{name} non défini, source ignorée ({out})")
            continue
        print(f"== {name} ({kind}) -> {out}")
        try:
            if kind == "xlsx":
                export_xlsx(url, out)
            elif kind == "file":
                os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
                with open(out, "wb") as f:
                    f.write(load_bytes(url))
            else:
                raise ValueError(f"type inconnu : {kind}")
        except Exception as e:  # une source cassée ne bloque pas les autres
            print(f"::error::{name} : {e}")
            failed.append(name)

    if failed:
        sys.exit(f"échec : {', '.join(failed)}")


if __name__ == "__main__":
    main()
