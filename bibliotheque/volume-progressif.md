# Volume progressif

> **À quoi sert ce fichier :** décrire l'approche qui construit d'abord une large base d'endurance, en augmentant la charge par petites marches.
> **Mis à jour par :** personne (contenu du projet). Propose une amélioration par une pull request.

> 📎 Page de référence reprise du projet `running-coach-athletes`, écrite pour un coureur : ici, elle sert au coach et à l'assistant comme bibliothèque, jamais à la place de la philosophie du coach.

## En une phrase

Tu construis d'abord un gros socle d'endurance facile, tu augmentes la charge par petites marches, et tu t'accordes régulièrement une semaine plus légère pour que ton corps encaisse le travail.

## Les principes

- **La base d'abord** : la majorité du volume se court en endurance fondamentale. L'intensité arrive ensuite, par petites touches, puis le spécifique à l'approche de la course.
- **Une seule chose augmente à la fois** : d'abord le nombre de séances, puis leur durée, puis la sortie longue, et seulement ensuite l'intensité. Pas tout en même temps.
- **Par paliers** : 2 à 3 semaines de hausse, puis 1 semaine allégée (environ un quart à un tiers de volume en moins) pour assimiler. On repart ensuite d'un cran au-dessus.
- **La « règle des 10 % » est un repère, pas une loi.** Augmenter de 10 % par semaine au maximum est prudent, mais les preuves sont faibles : chez des débutants, un programme bâti sur cette règle n'a pas réduit les blessures (Buist, 2008). En revanche, une hausse de plus de 30 % en deux semaines semble associée à davantage de certaines blessures (Nielsen, 2014). Retiens surtout : **pas de gros saut**.
- **Charge récente contre charge habituelle** : le coach compare ta dernière semaine à la moyenne de tes 4 dernières. Un pic soudain est plus risqué qu'une charge élevée construite progressivement (Gabbett, 2016). Le ratio chiffré entre les deux est très discuté par les chercheurs : c'est un indice parmi d'autres, jamais un chiffre magique.
- **La sortie longue grandit doucement** : 5 à 10 minutes de plus toutes les une à deux semaines. Repère courant : elle ne dépasse pas environ 25 à 30 % du volume de la semaine.
- **La régularité bat l'héroïsme** : 4 séances chaque semaine valent mieux que 6, puis 2, puis 5. Le sommeil, le jour de repos et la semaine allégée font partie de l'entraînement.

## Une semaine type

*Exemple pour un coureur à 5 séances, en phase de base (foncier). À adapter à ton profil et à ta course.*

| Jour | Séance | But |
|---|---|---|
| Lundi | Repos | Récupérer |
| Mardi | Footing 45 min facile + 6 lignes droites | Volume, foulée |
| Mercredi | Footing 50 min facile, ou PPG 30 min | Volume ou renforcement |
| Jeudi | 15 min facile, 20 min allure tempo, 10 min facile | Une touche d'intensité |
| Vendredi | Repos | Souffler |
| Samedi | Footing 40 min facile | Volume |
| Dimanche | Sortie longue 1 h 20, à allonger de 5 à 10 min toutes les 1 à 2 semaines | Endurance |

Exemple de bloc sur 4 semaines (volume total) : 30 km → 33 km → 36 km → 26 km (allégée), puis 34 km pour repartir.

## Pour qui

- Les débutants et tous ceux qui reprennent une saison.
- La préparation d'un marathon ou d'un ultra, dont la base fait la moitié du travail.
- Les coureurs qui se blessent souvent quand ils augmentent.
- Ceux qui veulent passer de 3 à 4 ou 5 séances par semaine.

## Pas pour qui / précautions

- **Plus n'est pas toujours mieux.** Ton plafond dépend aussi de ton travail, de ta famille, de ton sommeil. Le bon volume est celui que tu tiens sans t'épuiser.
- **Blessure en cours** : commence par `philosophie/retour-de-blessure.md`, et seulement avec l'accord d'un professionnel de santé.
- **Débutant complet** : commence par la régularité, éventuellement en alternant marche et course.
- **Peu de temps disponible** : si le volume ne peut pas monter, on joue plutôt sur la qualité des séances.
- **Plus de volume, plus de carburant** : mange suffisamment pour ce que tu fais. Une fatigue qui ne passe pas, des fractures de fatigue ou (pour une athlète) une perte des règles méritent l'avis d'un médecin.

## Signaux d'alerte

- La fatigue ne disparaît pas après la semaine allégée.
- FC au repos au-dessus de ta norme ou VFC en dessous, plusieurs jours d'affilée.
- À FC égale, ton allure facile ralentit d'une semaine à l'autre.
- Une petite douleur revient toujours au même endroit (tibia, genou, tendon d'Achille).
- Sommeil dégradé, irritabilité, moins d'envie de courir.
- Un saut de plus de 30 % d'une semaine sur l'autre, hors retour au volume habituel après une semaine allégée.

## Comment l'assistant s'en sert ici

- **Ce n'est pas la philosophie du coach.** L'assistant applique d'abord `athletes/<slug>/philosophie.md`, puis `coach/philosophie/`.
- **Pendant l'arrivée** (`conversations/arrivee-coach.md`), si les plans observés dans Nolio ressemblent à cette approche, il le dit en une phrase pour aider le coach à formuler sa propre méthode.
- **En alternative** : quand le coach demande « et si on faisait autrement ? », l'assistant peut s'appuyer sur cette page, en la présentant à part et marquée « hors philosophie du coach », avec ses sources.
- **Signaux d'alerte** : les signaux listés plus haut peuvent nourrir les seuils de `coach/criteres-alertes.md`, si le coach le valide.

## Sources

- Buist I., Bredeweg S. W., van Mechelen W., Lemmink K. A. P. M., Pepping G.-J., Diercks R. L. (2008). No effect of a graded training program on the number of running-related injuries in novice runners: a randomized controlled trial. *The American Journal of Sports Medicine*, 36(1), 33–39. https://doi.org/10.1177/0363546507307505
- Nielsen R. Ø., Parner E. T., Nohr E. A., Sørensen H., Lind M., Rasmussen S. (2014). Excessive progression in weekly running distance and risk of running-related injuries: an association which varies according to type of injury. *Journal of Orthopaedic & Sports Physical Therapy*, 44(10), 739–747. https://doi.org/10.2519/jospt.2014.5164
- Gabbett T. J. (2016). The training—injury prevention paradox: should athletes be training smarter and harder? *British Journal of Sports Medicine*, 50(5), 273–280. https://doi.org/10.1136/bjsports-2015-095788
- Impellizzeri F. M., Tenan M. S., Kempton T., Novak A., Coutts A. J. (2020). Acute:chronic workload ratio: conceptual issues and fundamental pitfalls. *International Journal of Sports Physiology and Performance*, 15(6), 907–913. https://doi.org/10.1123/ijspp.2019-0864 — les limites du ratio charge aiguë / chronique.
- Daniels J. (2022). *Daniels' Running Formula*, 4e édition. Human Kinetics. https://us.humankinetics.com/products/daniels-running-formula-4th-edition
- Pfitzinger P., Douglas S. (2019). *Advanced Marathoning*, 3e édition. Human Kinetics (une 4e édition est parue depuis). https://us.humankinetics.com/products/advanced-marathoning-3rd-edition
