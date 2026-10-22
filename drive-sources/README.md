# Sources Google Drive

> **À quoi sert ce fichier :** comment synchroniser des documents Google Drive dans le repo (niveau expert).
> **Mis à jour par :** contenu du projet ; les fichiers synchronisés sont écrits par la GitHub Action.

Contenu **synchronisé automatiquement** depuis Google Drive. Ne pas l'éditer à la main : toute
modification serait écrasée à la prochaine synchro. Pour corriger un contenu, le modifier dans Drive.

- Workflow : `.github/workflows/sync-drive.yml`. Il tourne chaque nuit à 03:00 UTC, à chaque
  modification de `sources.json`, ou à la main (Actions → Sync Google Drive → Run workflow).
- Scripts : `scripts/sync_drive.py` (lit `sources.json`) et `scripts/sync_sheet.py`.
- Organisation : `athletes/<slug>/…` pour ce qui concerne un athlète (`races/`, `strength/`,
  `tests/`, `wellbeing/`…), et `plans/` pour les documents de méthode communs.

## Sources actuelles

Aucune : `sources.json` est vide. Exemple d'entrée, pour le récap de courses d'un athlète :

```json
{
  "secret": "DRIVE_<PRENOM>_COURSES_XLSX_URL",
  "type": "xlsx",
  "out": "drive-sources/athletes/<slug>/races",
  "description": "Récap courses de <Prénom> (Google Sheet, un CSV par onglet)"
}
```

## Ajouter une source

1. **Obtenir une URL de téléchargement.**
   - Google Sheet ou Excel : Fichier → Partager → *Publier sur le web* → Classeur entier,
     format **.xlsx** → copier le lien. Un Excel (.xlsx) déposé sur le Drive doit d'abord être
     ouvert puis enregistré au format Google Sheets.
   - Google Doc : Partager → « Tous les utilisateurs disposant du lien » (lecteur), puis utiliser
     `https://docs.google.com/document/d/<ID>/export?format=md`, avec le type `file`.
2. **Stocker l'URL dans GitHub** : Settings → Secrets and variables → Actions.
   - Pour un **document de santé ou d'athlète, utiliser un *secret*.** L'URL est la seule
     protection du document : quiconque l'a peut le lire.
   - Une *variable* suffit pour du contenu non sensible.
3. **Déclarer la source dans `sources.json`** : nom du secret, type (`xlsx` → un CSV par onglet
   dans un dossier ; `file` → un fichier) et chemin de sortie `out`.
4. Pousser sur `main` : le workflow se lance tout seul.

Une source déclarée mais sans secret est ignorée avec un avertissement. Une source en erreur
n'empêche pas les autres d'être synchronisées.
