# Personnaliser ton assistant

> **À quoi sert ce fichier :** adapter l'assistant à ta façon de coacher, du plus simple (le lui dire) au plus avancé (ajouter une automatisation).
> **Mis à jour par :** contenu du projet.

## Le plus simple : le lui dire

Chaque tâche finit par une question pour s'améliorer. Réponds-y, ou dis à tout moment :
- « Ne commente pas les footings conformes. »
- « Chez moi, une alerte RPE, c'est dès +2. »
- « Mes messages sont plus courts que ça, 3 lignes max. »

L'assistant note le retour dans `coach/retours-agent.md`, propose l'ajustement, et l'applique quand tu valides. Une règle d'entraînement va dans `coach/philosophy/`, un seuil dans `coach/criteres-alertes.md`, une règle de ton dans `coach/philosophy/communication.md`.

## Les réglages courants

| Je veux… | Où | Comment |
|---|---|---|
| changer l'heure du radar ou de la revue | dans Claude | modifie la tâche planifiée (et le mémo de `reglages.md`) |
| ne plus avoir de brouillons quotidiens | `reglages.md` | `brouillons_quotidiens: non` |
| un seuil d'alerte différent pour un athlète | `athletes/<slug>/profil.md` › Points de vigilance | « RPE : alerte dès +2 pour elle » |
| adapter ma méthode pour un athlète | `athletes/<slug>/philosophie.md` | ou « Revoyons la philosophie de Marc » |
| mettre un athlète en pause | `athletes/index.md` et son profil | `statut: pause` |
| revoir toute ma philosophie | conversation | « Revoyons ma philosophie » (arrivée, bloc 2) |
| ajouter un protocole de blessure | `injuries/` | copie `_template-protocole.md`, idéalement validé avec un kiné |
| ajouter une séance de renfo type | `strength/<sport>/` | copie `strength/_template-seance.md` |
| passer au niveau 5 (écriture dans Nolio) | permissions Nolio + `reglages.md` | `AUTOMATISATION.md` › Niveau 5 |

## Modifier un prompt

Tout est en Markdown, modifiable sur GitHub (✏️, puis « Commit changes »). Le format d'un message est dans la section « Format » du fichier `automations/` concerné. Garde la ligne `---` : la tâche exécute tout ce qui la suit.

## Ajouter une automatisation

Par exemple, un point « préparation de course » chaque mercredi.
1. Copie la structure d'un fichier existant (`automations/bilan-mensuel.md` est le plus court) : titre, en-tête, tableau de réglages, ligne `---`, prompt, journal technique.
2. Choisis un nom de tâche pour `automations/runs.md`, et ajoute-le dans `MAX_AGE` de `scripts/controle.py`.
3. Ajoute une ligne au mémo de `reglages.md`, et une commande dans `.claude/commands/` si tu veux la lancer à la main.
4. Crée la tâche planifiée avec le prompt talon (`AUTOMATISATION.md`).

## Brancher tes Google Sheets (niveau expert)

Récap de courses, programmes de renfo, suivis : `drive-sources/README.md`. Les documents sont synchronisés chaque nuit dans le repo par une GitHub Action, et les liens restent dans les secrets GitHub.

## Récupérer les améliorations du projet

Un repo créé depuis un template ne se met pas à jour tout seul. Recopie les fichiers qui t'intéressent (`automations/`, `conversations/`, `docs/`, `CLAUDE.md`) depuis le projet d'origine. Compare avant d'écraser si tu les avais modifiés. Ne touche pas à tes données : `coach/`, `athletes/`, `reports/`, `etat.md`, `reglages.md`.
