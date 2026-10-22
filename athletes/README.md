# Athlètes

> **À quoi sert ce fichier :** comment sont rangés les athlètes. Un dossier par athlète, créé automatiquement par l'arrivée à partir de Nolio.
> **Mis à jour par :** contenu du projet.

Un dossier par athlète : `athletes/<prenom-nom>/` (slug en minuscules, sans accents), copié depuis `_template/`.
Il n'y a pas de création à la main : la conversation d'arrivée (`conversations/arrivee-coach.md`) liste les athlètes du coach dans Nolio et crée leurs dossiers. Un athlète ajouté plus tard dans Nolio est repéré par le radar du matin, qui propose de faire sa fiche.

| Fichier | Rôle | Mis à jour |
|---|---|---|
| `profil.md` | identité sportive, `nolio_id`, consentement, objectifs, repères, forces et limites | arrivée, fiche athlète, coach |
| `philosophie.md` | comment le coach adapte sa méthode à cet athlète (les écarts seulement) | fiche athlète, coach |
| `sante.md` | antécédents, pathologies en cours, sommeil, récupération | fiche athlète, coach, alertes (après accord) |
| `tests.md` | historique des tests et bilans | après chaque test |
| `journal.md` | notes datées, ajouts uniquement (coach + agent) | au fil de l'eau |
| `plan-<saison>.md` (facultatif) | leviers, rétroplanning, questions ouvertes de la saison | à chaque changement de phase |

Le tableau de bord du groupe est dans [`index.md`](index.md).
Les données brutes issues de Drive (bilans PDF, fiches) restent dans `drive-sources/`, citées par lien plutôt que recopiées.
