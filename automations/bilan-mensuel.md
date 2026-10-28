# Bilan mensuel — prompt de la tâche planifiée

> **À quoi sert ce fichier :** le point du mois : la progression de chaque athlète vers ses objectifs, les tests à planifier, et le ménage de la mémoire.
> **Mis à jour par :** contenu du projet ; l'agent l'ajuste quand le coach valide un retour (`coach/retours-agent.md`).

| Réglage de la tâche | Valeur conseillée |
|---|---|
| Fréquence | chaque mois, le 1er |
| Heure | 08:07 |
| Repo | le repo du coach |
| Connecteurs | Nolio (compte coach). Décoche tous les autres. |
| Modèle | un modèle plus capable (ex. Opus) |
| Écrit | `reports/monthly/AAAA-MM.md`, `athletes/index.md`, `coach/retours-agent.md`, `automations/runs.md` |

---

Tu es l'assistant du coach. Lis `CLAUDE.md`, `reglages.md`, `etat.md`, `athletes/index.md` et `coach/retours-agent.md`. Mois analysé = le mois précédent.

C'est une tâche planifiée : tu n'écris jamais dans Nolio et tu n'envoies rien à personne.

## 1. Collecte

- **Les bilans hebdo du mois** (`reports/weekly/`) : ils résument les semaines. N'ouvre un journal d'athlète que si un bilan y renvoie.
- **Nolio, par athlète suivi** : totaux du mois par rapport au mois précédent, records et compétitions du mois.
- **Profil de chaque athlète** : objectifs et échéances, tests passés (`tests.md`).
- **Journal technique** : les lignes du mois dans `automations/runs.md`.

## 2. Écrire `reports/monthly/AAAA-MM.md`

- **Le groupe** : volume, régularité, alertes du mois, blessures en cours.
- **Par athlète** (3 lignes) : où il en est par rapport à son objectif (🟢 / 🟠 / 🔴), sa tendance sur 4 semaines, le point du mois prochain.
- **Tests à planifier** : les athlètes dont le dernier test (`tests.md`) date de plus de 3 mois, ou qui changent de phase. Propose le protocole de `assessments/`.
- **Objectifs à revoir** : un objectif devenu irréaliste ou dépassé, avec une proposition. Elle ne s'applique qu'après accord du coach.
- **Fiches à compléter** et **athlètes sans consentement** : la liste.
- **Côté technique** : tâches en échec ou partielles, et la source le plus souvent en cause.

## 3. Ménage de la mémoire

- **`coach/retours-agent.md`** : vérifie que chaque retour du mois est appliqué, condense les lignes de plus d'un mois en règles, et vise moins de 4 Ko.
- **`automations/runs.md`** : garde les 2 derniers mois.
- **`athletes/index.md`** : mets à jour la phase et la prochaine course de chaque athlète.

## 4. Message (5 lignes maximum)

```
## 🗓️ Bilan de <mois>
👥 <n> athlètes · <volume> · <évolution>
🎯 En bonne voie : … · À revoir : …
🧪 Tests à planifier : …
🔧 Qu'est-ce que tu veux que je change pour le mois prochain ?
```

## 5. Quand le coach répond (même session)

- Il valide un changement d'objectif : mets à jour le profil de l'athlète, et ajoute une ligne à son journal.
- Un retour sur l'assistant : `coach/retours-agent.md`.
- Commit et push après chaque écriture.

## 6. Journal technique

Ajoute à la fin de `automations/runs.md` : `AAAA-MM-JJ HH:MM | bilan-mensuel | ok/partiel/échec | sources en échec ou —`. Puis `git pull --rebase`, commit `bilan: AAAA-MM`, push sur `main`.

## Plateforme : Nolio

- Totaux mensuels par athlète, records, compétitions. Voir `docs/nolio.md`.
