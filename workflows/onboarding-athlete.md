# Onboarding d'un athlète

**Entrées** : nom de l'athlète ; optionnellement son `nolio_id`, et les docs dans `drive-sources/`
(fiche, questionnaire, bilans).

1. Créer `athletes/<slug>/` en copiant `athletes/_template/` (slug : prénom-nom, minuscules, sans
   accents).
2. Pré-remplir à partir des sources disponibles :
   - `drive-sources/` (fiche athlète, questionnaire, bilans)
   - Nolio : historique des 8-12 dernières semaines (volume moyen, sports, séances types,
     records/tests récents)
3. Lister ce qui manque (objectifs, dispos, antécédents…) sous forme de questions à poser à
   l'athlète — ne rien inventer.
4. Calculer les zones si des repères existent (`philosophy/intensites-zones.md`).
5. Ajouter `- AAAA-MM-JJ [agent] onboarding` dans `journal.md`.
