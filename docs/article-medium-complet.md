# Article Medium « complet » côté coach — le plan

> **À quoi sert ce fichier :** le plan de l'article long : l'assistant complet du coach, ses 6 niveaux, l'arrivée qui remplit le repo toute seule, et les garde-fous qui protègent les athlètes et le plan du coach.
> **Mis à jour par :** le mainteneur du projet.

## L'angle

Un assistant qui connaît chaque athlète comme son coach le connaît : son enjeu, ses forces, ses blessures, et la façon dont le coach adapte sa méthode pour lui. Il s'installe tout seul : on branche Nolio, on dit « Lance mon arrivée », et il interviewe le coach. Le coach garde la main sur tout.

## Titres possibles

1. « Mon assistant de coaching connaît mes 20 athlètes. Il a commencé par m'interviewer. »
2. « Claude × Nolio : 6 niveaux pour automatiser le suivi de ses athlètes, sans jamais lâcher le plan »
3. « Ce que j'ai appris en construisant un assistant pour coachs d'endurance »

## Structure (≈ 10 min de lecture)

1. **L'accroche** : le même matin vu par le radar express et par le radar complet (`examples/sample-coach/outputs/`). Léo : 🟠 pour l'un, 🔴 pour l'autre. La différence, c'est la mémoire.
2. **L'idée** : un repo-mémoire (coach, athlètes, protocoles) + Nolio (les données) + Claude (l'exécution). Schéma 1 de `docs/architecture.md`.
3. **L'arrivée**, le cœur du projet (schéma 2) :
   - les athlètes découverts dans Nolio ;
   - la philosophie observée dans les plans, puis confirmée ;
   - une fiche par athlète, avec la philosophie adaptée.
   Extrait de `examples/sample-coach/outputs/arrivee-extrait.md`.
4. **Les 6 niveaux** (`AUTOMATISATION.md`), du radar express à l'écriture dans Nolio.
5. **Les garde-fous** :
   - consentement des athlètes ;
   - jamais de message envoyé en leur nom ;
   - jamais de diagnostic ;
   - les trois verrous d'écriture (schéma 7).
6. **Rester économe avec 30 athlètes** : trier d'abord, détailler ensuite (schéma 4) ; `etat.md` ; un bilan hebdo qui s'appuie sur les radars.
7. **Ce que j'ai appris** : 4 ou 5 entrées de `docs/journal-de-construction.md`.
8. **Les limites** : pas un coach, pas un médecin ; la qualité des données ; le coût ; le cadre légal (consentement, données de santé, carte professionnelle du coach).
9. **L'appel** : le template, la checklist de test, et l'accompagnement pour les coachs qui veulent l'installer.

## Entrées du journal à mettre en avant

- 🧭 L'arrivée remplace le remplissage à la main.
- 🧭 Une philosophie à deux étages.
- ✅ Pas de consentement, pas d'analyse.
- ✅ Trier d'abord, détailler ensuite.
- ✅ Jamais de message envoyé à un athlète.

## Visuels

- Le radar complet sur téléphone, à côté du radar express.
- Les schémas « arrivée », « une journée », « quelle philosophie s'applique », « le plan reste celui du coach ».
- Un extrait de fiche athlète (`examples/sample-coach/athletes/`).

## Chiffres à mesurer avant de publier

- [ ] Temps de l'arrivée : blocs 1 à 4, puis par athlète.
- [ ] Faux positifs du radar sur 2 semaines, avant et après réglage des seuils.
- [ ] Temps gagné par jour selon le coach testeur (avec son accord).
- [ ] Consommation mensuelle observée.

## Post LinkedIn (long)

> Le premier jour, mon assistant de coaching ne savait rien. Il a commencé par lire mes plans dans Nolio et m'a dit : « Tu fais du polarisé, 2 séances dures max, une semaine allégée toutes les 4 ? »
> Puis il m'a interviewé, athlète par athlète : son enjeu, ses forces, ses blessures, ce que je fais différemment avec lui.
> Aujourd'hui, à 7 h, il sait qu'une gêne au tibia chez Léo n'est pas une gêne comme les autres.
> Il n'écrit jamais à mes athlètes. Il ne touche pas à mes plans sans mon « je valide ».
> Le template est open source : 6 niveaux, du simple radar à l'assistant complet.
