# Brancher Claude sur Nolio et sur ce repo

Le repo apporte le contexte (athlètes, philosophie, workflows, sources Drive) ; le connecteur
Nolio apporte les données d'entraînement. Il faut les deux dans la même conversation Claude.

## 1. Le connecteur Nolio

Il faut un serveur MCP qui lise l'API Nolio. À date, celui qui a servi pour ce modèle est le
serveur communautaire [nico-b/nolio-mcp](https://github.com/nico-b/nolio-mcp) (licence MIT,
lecture seule). Il n'est pas officiel : relire son code avant de lui confier ses identifiants.

1. Déclarer une application sur le portail API de Nolio (<https://www.nolio.io/api/register/>),
   avec l'URL de redirection `http://localhost:9876/callback`. On obtient un *client ID* et un
   *client secret*.
2. Suivre le README du serveur : installation avec `uv`, puis `uv run nolio-auth` pour se
   connecter à Nolio. Les jetons sont enregistrés dans `~/nolio-credentials.json`, hors du repo.
3. Le déclarer dans **Claude Desktop** (fichier de config MCP) ou dans **Claude Code**
   (`claude mcp add nolio -- …`, commande donnée dans son README).

Outils fournis : `get_profile`, `get_workouts`, `get_planned_workouts`, `get_workout_streams`,
`get_notes`, `get_records`, `get_metrics` et `get_user_metadata`. Les deux derniers demandent une
autorisation API spéciale chez Nolio. **Limite** : il lit les données du compte connecté et ne
liste pas les athlètes d'un compte coach.

## 2. Le repo

### Option A — Projet Claude (le plus simple, lecture seule)

1. **Projects → New project**, par exemple « Coaching ».
2. **Instructions du projet** : coller le bloc ci-dessous, en remplaçant `[Prénom]`.
3. **Connaissances du projet** : Add content → **GitHub** → son repo privé. Tout sélectionner
   sauf `.github/` et `scripts/`.
4. **Avant chaque session**, resynchroniser le contenu GitHub du projet : la synchro Drive met
   `drive-sources/` à jour chaque nuit, et les fichiers du projet sont une copie figée.
5. Dans la conversation, **activer le connecteur Nolio**.

```text
Tu es l'assistant de coaching de [Prénom], coach d'endurance. Les fichiers du projet sont son
repo de coaching : lis d'abord CLAUDE.md et respecte ses règles.
Le connecteur Nolio donne les séances, records, notes et métriques ; le repo donne le contexte
(athletes/<slug>/, philosophy/, workflows/, drive-sources/).
Pour une demande qui correspond à un workflow de workflows/, suis-le étape par étape.
Tu n'as pas d'accès en écriture au repo : quand un workflow demande d'écrire un fichier, rends
le fichier complet dans un bloc de code avec son chemin, prêt à être copié.
Réponds en français, de façon concise.
```

Limite : le projet n'écrit pas dans le repo. Les rapports produits sont à recopier.

### Option B — Claude Code (lecture + écriture)

Claude Code ouvert sur le repo, avec le connecteur Nolio déclaré :
- les commandes `/check-quotidien`, `/bilan-hebdo`, `/bilan-progression`… marchent directement ;
- les rapports sont écrits dans `reports/` et peuvent être commités ;
- vérifier avec `/mcp` que le connecteur Nolio est bien connecté.

## 3. Premiers pas

1. « Récupère mon profil Nolio et donne-moi mon identifiant » → le reporter dans
   `athletes/<slug>/profil.md` (`nolio_id`).
2. « Exécute `workflows/onboarding-athlete.md` pour <prénom nom> ».
3. Au quotidien : « Exécute `workflows/check-quotidien.md` ».
4. En fin de saison : « Exécute `workflows/bilan-progression.md` pour <slug> ».
