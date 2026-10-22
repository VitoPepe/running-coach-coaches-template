# Nolio simulé — les données de la démo

> **À quoi sert ce fichier :** exemple fictif — les données que le connecteur Nolio renverrait pour le compte coach de Hugo. En mode démo (`plateforme: demo` dans `reglages.md`), l'assistant lit ce fichier à la place de Nolio.
> **Mis à jour par :** contenu du projet (exemple fictif). Ne pas le modifier pendant une démo : les autres fichiers de l'exemple en dépendent.

Date de démo (aujourd'hui) : 2026-10-24 (samedi)

**Conventions**
- Durées en h:mm ; FC en bpm ; D+ en mètres.
- Zones : temps en minutes `Z1-2 / Z3 / Z4-5`, calculé avec les zones de l'athlète enregistrées dans Nolio (modèle de Hugo, sur la FC seuil). Sophie : zones par défaut de Nolio, à partir d'une FC max estimée par formule.
- RPE de 0 à 10. « — » : non saisi, ou commentaire vide.
- « Prévu » : la séance planifiée par Hugo ce jour-là (durée et RPE prévu), ou « non prévue ».
- Le renforcement fait le même jour qu'une course n'est pas compté dans la durée.

## Athlètes du compte coach

| nolio_id | Athlète | Sport principal | Dans le compte depuis | Dernière activité | Prochaine compétition | Métriques du matin partagées |
|---|---|---|---|---|---|---|
| demo-1001 | Julie Martin | course sur route | 2025-01-06 | 2026-10-23 | 2027-02-21 — Semi fictif des Saules | oui (RMSSD, FC repos) |
| demo-1002 | Marc Dubois | trail | 2024-03-04 | 2026-10-22 | 2026-11-07 — Ultra des Aiguilles (fictif) | oui (RMSSD, FC repos) |
| demo-1003 | Léo Garcia | course sur route | 2025-09-01 | 2026-10-23 | 2027-04-25 — 10 km fictif des Tilleuls | non |
| demo-1004 | Sophie Bernard | course sur route | 2026-09-07 | 2026-10-23 | 2027-01-24 — 10 km fictif de la Galette | non |
| demo-1005 | Paul Lefèvre | trail | 2026-10-23 | 2026-10-23 | — | non |

Paul Lefèvre a rejoint le compte coach de Hugo le 2026-10-23 dans l'après-midi, après le radar du matin. Il n'est pas encore dans `athletes/index.md` de l'exemple.

## Séances prévues (2026-10-19 → 2026-10-27)

### Julie Martin (demo-1001)

| Date | Jour | Séance | Durée | Consigne | RPE prévu | Clé |
|---|---|---|---|---|---|---|
| 2026-10-19 | lun | Repos | — | — | — | |
| 2026-10-20 | mar | VMA courte 2 × 10 × 30/30 | 1:00 | 20 min d'échauffement, 2 séries de 10 × (30 s vite / 30 s trot), 3 min entre les séries, 15 min de retour au calme | 7 | oui |
| 2026-10-21 | mer | Footing 45 min (FC < 150) + PPG | 0:45 + 0:20 | Facile, alerte montre à 150 ; PPG mollets et gainage | 3 | |
| 2026-10-22 | jeu | Repos | — | — | — | |
| 2026-10-23 | ven | Footing 50 min (FC < 150) | 0:50 | Tranquille, alerte montre à 150 | 3 | |
| 2026-10-24 | sam | Footing 40 min + 6 lignes droites | 0:40 | Facile, 6 × 20 s en fin de footing | 3 | |
| 2026-10-25 | dim | Sortie longue 1 h 40 (FC < 150) | 1:40 | Tout en Z2, de l'eau toutes les 30 min | 4 | oui |
| 2026-10-26 | lun | Repos — début de la semaine allégée | — | — | — | |
| 2026-10-27 | mar | Seuil 2 × 8 min | 0:50 | 20 min d'échauffement, 2 × 8 min au seuil (FC 162 à 168), 2 min de récupération, 10 min de retour au calme | 6 | oui |

### Marc Dubois (demo-1002)

| Date | Jour | Séance | Durée | Consigne | RPE prévu | Clé |
|---|---|---|---|---|---|---|
| 2026-10-19 | lun | Repos | — | — | — | |
| 2026-10-20 | mar | Footing 1 h + PPG excentrique | 1:00 + 0:25 | Vallonné, facile ; squats lents, fentes descendues, 3 × 10 | 3 | |
| 2026-10-21 | mer | Côtes 10 × 1 min 30 + descentes rapides | 1:10 | 20 min d'échauffement ; 10 × 1 min 30 en côte (Z4), redescente rapide et relâchée ; 15 min de retour au calme | 7 | oui |
| 2026-10-22 | jeu | Footing 1 h | 1:00 | Facile, plat | 2 | |
| 2026-10-23 | ven | Repos | — | — | — | |
| 2026-10-24 | sam | Sortie longue 2 h 30 — travail de descente | 2:30 | 1 000 m de D+ et 1 000 m de D- (réduit le 2026-10-20, au lieu de 1 400 m) ; montées en Z2, en course et marche active ; 3 × 10 min de descente technique à allure course, en remontant tranquillement entre chaque ; 30 dernières min en Z1 ; bâtons et ravito de course (un gel toutes les 40 min) | 5 | oui — la dernière avant l'affûtage |
| 2026-10-25 | dim | Footing récup 40 min (facultatif) — début de l'affûtage | 0:40 | Très facile, plat, ou repos | 2 | |
| 2026-10-26 | lun | Repos | — | — | — | |
| 2026-10-27 | mar | Footing 1 h avec 5 × 1 min en côte | 1:00 | Facile, 5 × 1 min en côte (Z4) au milieu | 4 | |

### Léo Garcia (demo-1003)

| Date | Jour | Séance | Durée | Consigne | RPE prévu | Clé |
|---|---|---|---|---|---|---|
| 2026-10-19 | lun | Repos | — | — | — | |
| 2026-10-20 | mar | Course continue 25 min + renfo kiné | 0:25 + 0:30 | Z1-Z2, plat, chemin ; note ta gêne sur 10 | 3 | |
| 2026-10-21 | mer | Vélo 50 min | 0:50 | Z1-Z2 | 2 | |
| 2026-10-22 | jeu | Repos | — | — | — | |
| 2026-10-23 | ven | Course continue 30 min | 0:30 | Z1-Z2, plat, chemin ; première à 30 min (phase 2) ; note ta gêne sur 10 | 3 | |
| 2026-10-24 | sam | Vélo 45 min + renfo kiné | 0:45 + 0:30 | Z1-Z2 | 2 | |
| 2026-10-25 | dim | Course continue 30 min | 0:30 | Z1-Z2, plat, chemin ; note ta gêne sur 10 | 3 | |
| 2026-10-26 | lun | Repos | — | — | — | |
| 2026-10-27 | mar | Course continue 30 min + renfo kiné | 0:30 + 0:30 | Z1-Z2, plat, chemin ; note ta gêne sur 10 | 3 | |

### Sophie Bernard (demo-1004)

| Date | Jour | Séance | Durée | Consigne | RPE prévu | Clé |
|---|---|---|---|---|---|---|
| 2026-10-19 | lun | Repos | — | — | — | |
| 2026-10-20 | mar | Footing 35 min | 0:35 | Tout doux : tu dois pouvoir parler | 3 | |
| 2026-10-21 | mer | Repos | — | — | — | |
| 2026-10-22 | jeu | Footing 30 min + 5 lignes droites | 0:35 | Tout doux, 5 accélérations de 20 s à la fin | 3 | |
| 2026-10-23 | ven | Repos | — | — | — | |
| 2026-10-24 | sam | Sortie longue 55 min | 0:55 | Très facile, marche autorisée dans les côtes | 4 | oui |
| 2026-10-25 | dim | Repos | — | — | — | |
| 2026-10-26 | lun | Repos | — | — | — | |
| 2026-10-27 | mar | Footing 35 min | 0:35 | Tout doux | 3 | |

### Paul Lefèvre (demo-1005)

Aucune séance prévue : Hugo ne lui a pas encore écrit de plan.

## Activités réalisées (2026-10-12 → 2026-10-23)

### Julie Martin (demo-1001)

| Date | Séance | Prévu | Durée | Distance | D+ | FC moy | Z1-2 / Z3 / Z4-5 | RPE | Commentaire de l'athlète |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-13 | Seuil 3 × 8 min | 1 h 05 · RPE 7 | 1:05 | 12,6 km | 40 | 154 | 41 / 14 / 10 | 7 | Dur le dernier bloc, mais tenu. |
| 2026-10-14 | Footing 45 min (FC < 150) + PPG | 45 min · RPE 3 | 0:47 | 8,6 km | 30 | 149 | 35 / 12 / 0 | 3 | — |
| 2026-10-16 | Footing 50 min (FC < 150) | 50 min · RPE 3 | 0:50 | 9,1 km | 25 | 144 | 47 / 3 / 0 | 3 | Seule, tranquille. |
| 2026-10-17 | Footing 40 min + 6 lignes droites | 40 min · RPE 3 | 0:42 | 7,8 km | 20 | 143 | 39 / 2 / 1 | 3 | — |
| 2026-10-18 | Sortie longue 1 h 30 (FC < 150) | 1 h 30 · RPE 4 | 1:32 | 17,2 km | 120 | 146 | 85 / 7 / 0 | 4 | Bien, un peu lourde à la fin. |
| 2026-10-20 | VMA courte 2 × 10 × 30/30 | 1 h · RPE 7 | 0:58 | 11,0 km | 35 | 152 | 38 / 8 / 12 | 8 | Dure, la 2e série, il faisait froid. |
| 2026-10-21 | Footing 45 min (FC < 150) + PPG | 45 min · RPE 3 | 0:45 | 8,3 km | 30 | 146 | 41 / 4 / 0 | 3 | — |
| 2026-10-23 | Footing 50 min (FC < 150) | 50 min · RPE 3 | 0:50 | 9,6 km | 25 | 151 | 30 / 20 / 0 | 3 | Footing avec une copine du club, bonnes sensations ! |

### Marc Dubois (demo-1002)

| Date | Séance | Prévu | Durée | Distance | D+ | FC moy | Z1-2 / Z3 / Z4-5 | RPE | Commentaire de l'athlète |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-13 | Footing 1 h vallonné + PPG | 1 h · RPE 3 | 1:02 | 10,6 km | 310 | 131 | 60 / 2 / 0 | 3 | — |
| 2026-10-14 | Côtes longues 6 × 4 min | 1 h 15 · RPE 7 | 1:15 | 12,0 km | 640 | 146 | 47 / 10 / 18 | 7 | Bonnes jambes en montée. |
| 2026-10-15 | Footing 1 h | 1 h · RPE 2 | 0:58 | 10,2 km | 150 | 129 | 58 / 0 / 0 | 2 | — |
| 2026-10-17 | Sortie longue 3 h 30 — 1 800 m D+ | 3 h 30 · RPE 5 | 3:38 | 27,5 km | 1 820 | 136 | 196 / 20 / 2 | 6 | Montée nickel, un gel toutes les 40 min, ça passe. Dans la grande descente les quadris lâchent, j'ai fini la descente en marchant. |
| 2026-10-18 | Footing récup 1 h | 1 h · RPE 2 | 1:00 | 9,8 km | 200 | 127 | 60 / 0 / 0 | — | Jambes lourdes, quadris bien raides. |
| 2026-10-20 | Footing 1 h + PPG excentrique | 1 h · RPE 3 | 1:00 | 10,4 km | 220 | 130 | 59 / 1 / 0 | 3 | Quadris encore un peu raides au début, ok après 20 min. |
| 2026-10-21 | Côtes 10 × 1 min 30 + descentes rapides | 1 h 10 · RPE 7 | 1:10 | 11,2 km | 560 | 147 | 44 / 8 / 18 | 7 | Descentes plus fluides que d'habitude. |
| 2026-10-22 | Footing 1 h | 1 h · RPE 2 | 1:02 | 10,9 km | 140 | 128 | 62 / 0 / 0 | 2 | — |

2026-10-23 : repos prévu, aucune activité.

### Léo Garcia (demo-1003)

| Date | Séance | Prévu | Durée | Distance | D+ | FC moy | Z1-2 / Z3 / Z4-5 | RPE | Commentaire de l'athlète |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-12 | Course continue 20 min | 20 min · RPE 3 | 0:20 | 3,5 km | 10 | 142 | 20 / 0 / 0 | 3 | Premières 20 min d'affilée, rien au tibia. |
| 2026-10-13 | Vélo 45 min + renfo kiné | 45 min · RPE 2 | 0:45 | 17,8 km | 120 | 126 | 45 / 0 / 0 | 2 | — |
| 2026-10-14 | Course continue 20 min | 20 min · RPE 3 | 0:20 | 3,6 km | 10 | 141 | 20 / 0 / 0 | 3 | Nickel. |
| 2026-10-15 | Vélo 45 min | 45 min · RPE 2 | 0:47 | 18,9 km | 140 | 128 | 47 / 0 / 0 | — | — |
| 2026-10-16 | Course continue 25 min | 25 min · RPE 3 | 0:25 | 4,4 km | 15 | 144 | 25 / 0 / 0 | 3 | Rien au tibia. |
| 2026-10-17 | Renfo kiné | 30 min · RPE 3 | 0:30 | — | — | — | — | 3 | — |
| 2026-10-18 | Course continue 25 min | 25 min · RPE 3 | 0:25 | 4,5 km | 15 | 143 | 25 / 0 / 0 | 3 | — |
| 2026-10-20 | Course continue 25 min + renfo kiné | 25 min · RPE 3 | 0:26 | 4,6 km | 15 | 142 | 26 / 0 / 0 | 3 | RAS. |
| 2026-10-21 | Vélo 50 min | 50 min · RPE 2 | 0:50 | 20,3 km | 160 | 129 | 50 / 0 / 0 | — | — |
| 2026-10-23 | Course continue 30 min | 30 min · RPE 3 | 0:30 | 5,3 km | 15 | 146 | 30 / 0 / 0 | 4 | Petite gêne tibia gauche 3/10 en fin de séance. |

### Sophie Bernard (demo-1004)

| Date | Séance | Prévu | Durée | Distance | D+ | FC moy | Z1-2 / Z3 / Z4-5 | RPE | Commentaire de l'athlète |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-13 | Footing 35 min | 35 min · RPE 3 | 0:36 | 5,1 km | 20 | 152 | 30 / 6 / 0 | 4 | Dur de rester lente ! |
| 2026-10-15 | Footing 30 min + 4 lignes droites | 35 min · RPE 3 | 0:31 | 4,4 km | 10 | 150 | 26 / 4 / 1 | 4 | — |
| 2026-10-17 | Sortie longue 50 min | 50 min · RPE 4 | 0:50 | 6,9 km | 40 | 151 | 44 / 6 / 0 | 5 | Fière de moi, ma plus longue sortie ! |
| 2026-10-20 | Footing 35 min | 35 min · RPE 3 | 0:35 | 5,0 km | 15 | 149 | 32 / 3 / 0 | 4 | Mieux réussi à ralentir. |
| 2026-10-23 | Course à pied | non prévue | 0:32 | 4,6 km | 15 | 150 | 28 / 4 / 0 | — | — |

2026-10-22 : « Footing 30 min + 5 lignes droites » prévu, aucune activité, aucun commentaire.

### Paul Lefèvre (demo-1005)

**Consentement non recueilli : l'assistant ne lit pas ces lignes** tant que le profil de Paul n'indique pas `consentement: oui`. Elles sont là parce que Nolio les renvoie quand même (activités importées de sa montre à son arrivée), et pour montrer ce qu'un radar sans repo lirait sans se poser la question.

| Date | Séance | Prévu | Durée | Distance | D+ | FC moy | Z1-2 / Z3 / Z4-5 | RPE | Commentaire de l'athlète |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-19 | Sortie trail | non prévue | 1:05 | 10,2 km | 480 | 149 | non dispo | — | — |
| 2026-10-21 | Footing | non prévue | 0:45 | 8,0 km | 60 | 141 | non dispo | — | — |
| 2026-10-23 | Sortie trail | non prévue | 1:15 | 12,4 km | 610 | 150 | non dispo | — | Bonne sortie, pressé de commencer avec Hugo. |

## Métriques du matin (athlètes qui les partagent)

Seuls Julie et Marc partagent leurs métriques (`list_metrics`, clés `RMSSD` et `FCREPOS` ; pas de `SOMMEIL`). Norme : moyenne sur 60 jours, plus ou moins un écart-type.

### Julie Martin — norme : RMSSD 60 ms ± 6 (54 à 66), FC repos 48

| Date | RMSSD (ms) | FC repos (bpm) |
|---|---|---|
| 2026-10-18 | 61 | 48 |
| 2026-10-19 | 58 | 49 |
| 2026-10-20 | 62 | 48 |
| 2026-10-21 | 59 | 48 |
| 2026-10-22 | 60 | 47 |
| 2026-10-23 | 56 | 49 |
| 2026-10-24 | 55 | 50 |

### Marc Dubois — norme : RMSSD 72 ms ± 7 (65 à 79), FC repos 45

| Date | RMSSD (ms) | FC repos (bpm) |
|---|---|---|
| 2026-10-18 | 66 | 47 |
| 2026-10-19 | 69 | 46 |
| 2026-10-20 | 71 | 45 |
| 2026-10-21 | 74 | 45 |
| 2026-10-22 | 69 | 46 |
| 2026-10-23 | 73 | 45 |
| 2026-10-24 | 75 | 44 |

## Compétitions à venir

| Athlète | Date | Course | Distance, D+ | Priorité |
|---|---|---|---|---|
| Marc Dubois | 2026-11-07 | Ultra des Aiguilles (fictif) | 75 km, 4 200 m | A |
| Sophie Bernard | 2027-01-24 | 10 km fictif de la Galette | 10 km | B |
| Julie Martin | 2027-02-21 | Semi fictif des Saules | 21,1 km | B |
| Sophie Bernard | 2027-03-21 | Semi fictif des Marais | 21,1 km | A |
| Julie Martin | 2027-04-11 | Marathon fictif du Lac | 42,2 km | A |
| Léo Garcia | 2027-04-25 | 10 km fictif des Tilleuls | 10 km | A |

## Records

| Athlète | Distance | Temps | Date | Course |
|---|---|---|---|---|
| Julie Martin | 10 km | 45:20 | 2025-11-16 | 10 km fictif d'automne |
| Julie Martin | Semi-marathon | 1:38:40 | 2026-03-15 | Semi fictif du Printemps |
| Julie Martin | Marathon | 3:41:05 | 2025-04-13 | Marathon fictif du Lac |
| Marc Dubois | Marathon | 3:18:30 | 2024-10-27 | Marathon fictif d'automne |
| Marc Dubois | Trail 45 km, 2 700 m D+ | 6:05:12 | 2026-06-14 | Trail fictif des Crêtes |
| Léo Garcia | 5 km | 20:30 | 2026-04-12 | 5 km fictif du Parc |
| Léo Garcia | 10 km | 43:12 | 2026-05-17 | 10 km fictif des Tilleuls |
| Sophie Bernard | — | — | — | aucune course pour l'instant |
