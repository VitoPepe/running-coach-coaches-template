# Athlètes

Un dossier par athlète : `athletes/<prenom-nom>/` (slug en minuscules, sans accents).
Créer avec `/nouvel-athlete` ou copier `_template/`.

| Fichier | Rôle | Mis à jour |
|---|---|---|
| `profil.md` | Identité sportive, `nolio_id`, objectifs, zones, disponibilités | À chaque changement d'objectif / test |
| `sante.md` | Antécédents, pathologies en cours, nutrition, sommeil | À chaque événement santé |
| `tests.md` | Historique des tests et bilans (tableau) | Après chaque test |
| `journal.md` | Notes datées, en ajout uniquement (coach + agent) | Au fil de l'eau |
| `plan-<saison>.md` (optionnel) | Leviers, rétroplanning, questions ouvertes de la saison | À chaque changement de phase |

Les données brutes issues de Drive (bilans PDF, fiches) restent dans `drive-sources/` ;
on y fait référence par lien plutôt que de les recopier.
