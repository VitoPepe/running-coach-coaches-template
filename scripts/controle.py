#!/usr/bin/env python3
"""Contrôle du coach : lancé chaque nuit par la GitHub Action « Contrôle du coach » et par le bilan hebdo.

Vérifie :
- automations/runs.md : chaque tâche déjà lancée au moins une fois a tourné récemment,
  et sa dernière exécution (depuis hier) n'est ni partielle ni en échec ;
- etat.md : mis à jour il y a 3 jours au plus, dès que le débrief du soir a déjà tourné ;
- les chemins de fichiers du repo cités entre backticks ou en lien Markdown existent.

Sortie : la liste des problèmes (code 1 s'il y en a), rien sinon.
Aucune dépendance : Python 3 standard.
"""
import datetime
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TODAY = datetime.date.today()
MAX_AGE = {"brief": 1, "debrief": 1, "bilan-hebdo": 8, "bilan-mensuel": 32}
problems = []


def runs():
    path = ROOT / "automations/runs.md"
    if not path.exists():
        return {}
    latest = {}  # tâche -> (date, statut, détail) de la dernière exécution
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(\d{4}-\d{2}-\d{2}) [\d:]+ \| ([\w-]+) \| (\w+) \| (.*)$", line)
        if not m:
            continue
        try:
            day = datetime.date.fromisoformat(m.group(1))
        except ValueError:
            problems.append(f"runs.md : date non ISO « {m.group(1)} »")
            continue
        task, status, detail = m.group(2), m.group(3), m.group(4).strip()
        if task not in latest or day >= latest[task][0]:
            latest[task] = (day, status, detail)
    for task, (day, status, detail) in latest.items():
        if status != "ok" and (TODAY - day).days <= 1:
            problems.append(f"runs.md : {task} du {day} en {status} — {detail}")
        if task in MAX_AGE and (TODAY - day).days > MAX_AGE[task]:
            problems.append(f"runs.md : pas de {task} depuis le {day}")
    return latest


def etat(latest):
    if "debrief" not in latest:
        return  # le débrief n'a jamais tourné : rien à vérifier
    text = (ROOT / "etat.md").read_text(encoding="utf-8")
    m = re.search(r"Dernière mise à jour : (\d{4}-\d{2}-\d{2})", text)
    if not m:
        problems.append("etat.md : date de « Dernière mise à jour » absente ou pas au format AAAA-MM-JJ")
        return
    day = datetime.date.fromisoformat(m.group(1))
    if (TODAY - day).days > 3:
        problems.append(f"etat.md : pas mis à jour depuis le {day}")


def broken_paths():
    pattern = re.compile(r"`([\w./-]+\.(?:md|py|yml))`|\]\(([\w./-]+\.(?:md|py|yml))(?:#[^)]*)?\)")
    for md in ROOT.rglob("*.md"):
        rel = md.relative_to(ROOT)
        if rel.parts[0] in {".git", "journal", "bilans"}:
            continue
        for a, b in pattern.findall(md.read_text(encoding="utf-8")):
            target = a or b
            if "AAAA" in target or "/" not in target:
                continue  # modèle de nom (AAAA-MM-JJ) ou nom de fichier seul
            if not (ROOT / target.split("/")[0]).is_dir():
                continue  # chemin qui ne vise pas ce repo
            if not ((ROOT / target).exists() or (md.parent / target).exists()):
                problems.append(f"{rel} : chemin introuvable `{target}`")


etat(runs())
broken_paths()
for p in problems:
    print("- " + p)
sys.exit(1 if problems else 0)
