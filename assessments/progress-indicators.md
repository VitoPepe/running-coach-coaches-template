# Indicateurs de progression

> **À quoi sert ce fichier :** les indicateurs à croiser pour savoir si un athlète progresse d'une saison à l'autre.
> **Mis à jour par :** contenu du projet, ajustable par le coach.

**Question** : un athlète progresse-t-il d'une saison à l'autre, en trail comme sur route ?

**Principe** : les courses seules ne suffisent pas. Il y en a peu par an, les parcours changent,
et l'athlète ne court pas toujours à fond. On croise donc trois familles d'indicateurs, de la plus
fiable à la plus fragile, et on sépare toujours **la forme** (la capacité) de **l'exécution du
jour** (nutrition, départ, motivation, conditions).

## 1. En course : comparer à conditions égales

| Indicateur | Source | Ce qu'il mesure | Limites |
|---|---|---|---|
| **Même course d'une année sur l'autre** : temps, VAP, FC moyenne, RPE | récap courses (`drive-sources/athletes/<slug>/races/`) | La comparaison la plus propre | Parcours modifié, météo, stratégie (à fond ou en gestion) |
| **Équivalences route** : ramener 5k, 10k et semi à un 10k équivalent (formule de Riegel `T2 = T1 × (D2/D1)^1.06`, ou VDOT) | récap courses | Compare des distances différentes | Moins fiable au-delà du semi |
| **VAP par tranche** : distance (< 25 km, 25-45 km, > 45 km) × technicité | récap courses | Allure trail neutralisée du D+ | La VAP Garmin sous-estime le coût du technique et des descentes |
| **Efficacité cardiaque** : VAP rapportée à la FC moyenne | récap courses | Va-t-on aussi vite avec moins de FC ? | **À lire avec le RPE** : une FC basse peut traduire un gain d'efficacité ou une FC bridée par la fatigue |
| **Indicateurs externes** : index UTMB / ITRA, écart en % au vainqueur | utmb.world, itra.run, résultats | Tient compte du niveau du plateau et des conditions | L'écart au 1er dépend de qui est venu |

**Règles de lecture**
- Une course courue « en gestion » ne mesure pas le maximum : on la compare à une autre course en
  gestion, pas à une course à fond.
- VAP stable avec FC et RPE en baisse : progrès probable **si** la FC sait encore monter à l'effort
  maximal. Sinon, la piste est la fatigue.
- Ne jamais conclure sur une seule paire de courses.

## 2. À l'entraînement : les séances de référence répétées (Nolio)

Plus nombreuses et mieux contrôlées que les courses : c'est là que se lit la tendance.

| Indicateur | Comment le mesurer | Progrès si… |
|---|---|---|
| **FC à allure fixe** | Footing d'endurance sur un parcours plat de référence, même allure | La FC baisse à allure égale |
| **Découplage cardiaque** | Sortie longue : écart du ratio allure/FC entre la 1re et la 2e moitié | Le découplage diminue (< 5 % = bonne endurance) |
| **Vitesse ascensionnelle (m/h)** | Côte de référence ou tapis incliné, même protocole | Elle augmente (intègre le poids et la force) |
| **Allure des sorties longues** | Même type de SL, même phase de saison | Elle se maintient ou progresse. Une dégradation en série = saturation |
| **Tests** | Protocoles de ce dossier (VMA, seuil…) | Repères en hausse, résultats dans `athletes/<slug>/tests.md` |

## 3. Le contexte : ce qui explique les écarts

Ces facteurs ne mesurent pas la performance : ils servent à interpréter les écarts.
- Poids le jour J (colonne du récap courses), et composition corporelle si on l'a.
- Qualité de l'affûtage, sommeil, voyages, maladie avant la course (commentaires).
- Note d'exécution : sépare une mauvaise course d'une mauvaise forme.
- Volume annuel et charge des 4-6 semaines précédentes : la performance suit-elle le volume ?

## Livrable : le bilan de saison

Pour chaque saison (trail N, hiver route N/N+1…), un tableau par athlète :
1. Les paires de courses comparables, avec temps, VAP, FC et RPE, et leur évolution.
2. Les équivalences route (meilleur 10k équivalent de la saison).
3. L'évolution de l'index UTMB / ITRA.
4. Les tendances d'entraînement : FC à allure fixe, découplage, vitesse ascensionnelle.
5. Le contexte : poids, affûtages, notes d'exécution, blessures.
6. La conclusion : **progrès / stagnation / régression**, en séparant capacité et exécution, avec
   le niveau de confiance (combien de points de données).

Exemple : un même trail (29 km, ~1 600 m D+) couru deux ans d'écart : 2h40 → 2h36, VAP
4:29 → 4:15, FC moyenne 166 → 161, RPE 9 → 6, la seconde fois « en gestion ». Plus rapide pour
moins d'effort, mais si la FC max atteinte en course a aussi baissé d'une saison à l'autre, il
faut vérifier qu'elle sait encore monter avant de conclure à un gain d'efficacité.
