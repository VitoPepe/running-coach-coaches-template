# Journal technique des tâches planifiées

> **À quoi sert ce fichier :** exemple fictif — une ligne par exécution des tâches planifiées de Hugo, du 2026-10-18 au 2026-10-23. Même format que `automations/runs.md`.
> **Mis à jour par :** l'agent, à la fin de chaque tâche (ici : écrit pour l'exemple). Le bilan mensuel ne garde que les 2 derniers mois. Dans un vrai repo, contrôlé chaque nuit par `scripts/controle.py` (GitHub Action).

Format : `AAAA-MM-JJ HH:MM | tâche | statut | détail`
- tâche : `radar`, `revue`, `bilan-hebdo`, `bilan-mensuel`
- statut : `ok`, `partiel` (une source a échoué, mais la tâche est livrée), `échec`
- détail : les sources en échec (Nolio, git push…) ou `—`

Si une tâche n'a pas tourné depuis trop longtemps, ou si sa dernière exécution est en échec, le contrôle de la nuit échoue et GitHub envoie un mail au coach.

## Exécutions

2026-10-18 07:09 | radar | ok | —
2026-10-18 19:12 | bilan-hebdo | ok | —
2026-10-18 20:39 | revue | ok | —
2026-10-19 07:08 | radar | ok | —
2026-10-19 20:38 | revue | ok | —
2026-10-20 07:09 | radar | ok | —
2026-10-20 20:39 | revue | ok | —
2026-10-21 07:08 | radar | ok | —
2026-10-21 20:46 | revue | partiel | Nolio (timeout)
2026-10-22 07:09 | radar | ok | —
2026-10-22 20:38 | revue | ok | —
2026-10-23 07:08 | radar | ok | —
2026-10-23 20:40 | revue | ok | —
