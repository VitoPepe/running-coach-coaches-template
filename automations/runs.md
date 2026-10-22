# Journal technique des tâches planifiées

> **À quoi sert ce fichier :** une ligne par exécution de tâche planifiée, ajoutée par la tâche elle-même. Il permet de voir d'un coup d'œil si l'assistant tourne bien.
> **Mis à jour par :** l'agent, à la fin de chaque tâche. Le bilan mensuel ne garde que les 2 derniers mois. Contrôlé chaque nuit par `scripts/controle.py` (GitHub Action).

Format : `AAAA-MM-JJ HH:MM | tâche | statut | détail`
- tâche : `radar`, `revue`, `bilan-hebdo`, `bilan-mensuel`
- statut : `ok`, `partiel` (une source a échoué, mais la tâche est livrée), `échec`
- détail : les sources en échec (Nolio, git push…) ou `—`

Si une tâche n'a pas tourné depuis trop longtemps, ou si sa dernière exécution est en échec, le contrôle de la nuit échoue et GitHub envoie un mail au coach.

## Exécutions
