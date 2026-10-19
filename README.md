# Agent de coaching Nolio — modèle

Base de connaissances de coach à brancher sur **Claude**, avec le **connecteur MCP Nolio** et
une **synchro Google Drive**. Nolio fournit le *quoi* (séances planifiées / réalisées, métriques,
commentaires) ; ce repo fournit le *pourquoi* et le *comment* (contexte athlète, philosophie,
protocoles, routines de travail). L'agent croise les deux, propose ; le coach décide.

## Utiliser ce modèle

1. **Créer son repo à partir du modèle, en privé** (GitHub : *Use this template*, ou copie). Il
   contiendra des données de santé.
2. **Brancher Claude sur Nolio et sur le repo** : [`guides/brancher-claude.md`](guides/brancher-claude.md).
3. **Écrire sa philosophie** dans [`philosophy/`](philosophy/) et ses **seuils d'alerte** dans
   [`workflows/criteres-alertes.md`](workflows/criteres-alertes.md). C'est l'étape qui rend l'agent
   utile : sans elle, il applique des règles génériques.
4. **Créer une fiche par athlète** : `/nouvel-athlete <prénom nom>`, ou copier
   [`athletes/_template/`](athletes/_template/) vers `athletes/<prenom-nom>/`.
5. **Brancher ses Google Sheets** (récap courses, programmes, suivis) :
   [`drive-sources/README.md`](drive-sources/README.md).
6. **Lancer le premier check quotidien** : `/check-quotidien`.

## Structure

| Dossier | Contenu |
|---|---|
| [`athletes/`](athletes/) | Un dossier par athlète : profil, santé, tests, journal, plan de saison |
| [`philosophy/`](philosophy/) | Principes d'entraînement, zones, périodisation, façon de communiquer |
| [`strength/`](strength/) | Séances de renforcement par sport + transversal (gainage, mobilité) |
| [`injuries/`](injuries/) | Protocoles par pathologie (red flags, phases, reprise) |
| [`assessments/`](assessments/) | Protocoles de tests et indicateurs de progression |
| [`workflows/`](workflows/) | Routines de l'agent : check quotidien, bilan hebdo, analyse de séance, onboarding, bilan de progression |
| [`drive-sources/`](drive-sources/) | Docs Google Drive synchronisés chaque nuit (ne pas éditer à la main) |
| [`reports/`](reports/) | Sorties de l'agent : quotidien, hebdo, progression |
| [`guides/`](guides/) | Brancher Claude, bonnes pratiques |
| [`.claude/commands/`](.claude/commands/) | Raccourcis `/check-quotidien`, `/bilan-hebdo`, `/analyse-seance`, `/nouvel-athlete`, `/bilan-progression` |

Les règles de l'agent sont dans [`CLAUDE.md`](CLAUDE.md).

## Ce qui est à remplir

Les fichiers de `philosophy/`, `strength/`, `injuries/` et `assessments/` sont des **gabarits** :
titres et tableaux vides, à compléter avec ses propres méthodes. Les seuils de
`workflows/criteres-alertes.md` sont des valeurs par défaut à ajuster.

## Confidentialité

Ce repo contiendra des **données de santé** d'athlètes (pathologies, bilans, poids…) : repo
**privé** obligatoire, consentement des athlètes, liens Drive stockés en **secrets** GitHub, pas de
données d'identification inutiles (n° de sécu, adresse…).
