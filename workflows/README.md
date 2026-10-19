# Workflows

Procédures que l'agent exécute pas à pas. Chaque workflow précise : déclencheur, entrées,
étapes, sortie. Les commandes `.claude/commands/` ne font que les lancer.

| Workflow | Déclencheur | Commande | Sortie |
|---|---|---|---|
| [Check quotidien](check-quotidien.md) | Chaque matin | `/check-quotidien` | `reports/daily/AAAA-MM-JJ.md` |
| [Bilan hebdo](bilan-hebdo.md) | Dimanche soir / lundi | `/bilan-hebdo [athlète]` | `reports/weekly/AAAA-Wss.md` |
| [Analyse de séance](analyse-seance.md) | À la demande | `/analyse-seance <athlète> [date]` | Réponse + note journal |
| [Onboarding athlète](onboarding-athlete.md) | Nouvel athlète | `/nouvel-athlete <nom>` | `athletes/<slug>/` |
| [Bilan de progression](bilan-progression.md) | Fin de saison / à la demande | `/bilan-progression <athlète>` | `reports/progress/<slug>-AAAA-MM-JJ.md` |

Seuils et règles d'alerte communs : [criteres-alertes.md](criteres-alertes.md).

## Idées de workflows à ajouter
- Préparation de course (J-14 → J) : affûtage, stratégie d'allure et de ravito
- Retour de blessure : suivi des critères de phase d'un protocole `injuries/`
- Revue de plan : cohérence de la semaine à venir vs philosophie et disponibilités
- Messages athlètes : brouillons de retours hebdo dans le ton de `philosophy/communication.md`
