# Réglages

> **À quoi sert ce fichier :** les réglages de l'assistant (coach, plateforme, connecteurs, permissions) et l'avancement de l'arrivée.
> **Mis à jour par :** la conversation d'arrivée, puis le coach quand il veut changer un réglage (édition directe sur GitHub).

<!-- Remplace chaque _à compléter_, ou laisse la conversation d'arrivée le faire. Garde les noms de champs tels quels. -->

## Coach

- prenom_coach: _à compléter_
- structure: _à compléter_ <!-- indépendant, club, team… -->
- nombre_athletes: _à compléter_ <!-- rempli à partir de Nolio pendant l'arrivée -->

## Plateforme

- plateforme: nolio <!-- nolio | demo (demo = essayer avec le coach fictif, sans compte Nolio) -->
- permissions_nolio: _à compléter_ <!-- lecture (niveaux 1 à 4) | lecture+creation+suppression (niveau 5). Jamais « modification ». Voir docs/nolio.md -->

## Lieu et heure

- fuseau: Europe/Paris

## Connecteurs

- nolio: oui
- agenda: non <!-- Google Agenda du coach, en lecture : rendez-vous, déplacements -->
- drive: non <!-- synchro Google Drive → drive-sources/ (niveau expert) -->

## Brouillons pour les athlètes

- brouillons_quotidiens: oui <!-- la revue du soir prépare un commentaire par séance clé -->
- brouillons_hebdo: oui <!-- le bilan hebdo prépare un message par athlète -->

## Tâches planifiées actives

| Tâche planifiée | Fichier | Active | Heure | Jour |
|---|---|---|---|---|
| Radar du matin | `automations/radar-matin.md` | oui | 07:07 | tous les jours |
| Revue du soir | `automations/revue-soir.md` | oui | 20:37 | tous les jours |
| Bilan hebdo | `automations/bilan-hebdo.md` | oui | 19:07 | dimanche |
| Bilan mensuel | `automations/bilan-mensuel.md` | oui | 08:07 | le 1er du mois |

<!-- Mémo seulement : les vraies heures se règlent dans les tâches planifiées de Claude (AUTOMATISATION.md). -->

## Arrivée — progression

<!-- Cochée par conversations/arrivee-coach.md au fil de l'eau. La fiche de chaque athlète a son propre statut (athletes/index.md). -->

- [ ] 1. Toi, le coach
- [ ] 2. Ta philosophie générale
- [ ] 3. Tes seuils d'alerte
- [ ] 4. Tes athlètes, découverts dans Nolio
- [ ] 5. Les fiches des athlètes (une par une, voir `athletes/index.md`)
- [ ] 6. Réglages et premier état
