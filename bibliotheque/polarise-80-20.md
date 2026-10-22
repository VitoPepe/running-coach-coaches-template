# Polarisé 80/20

> **À quoi sert ce fichier :** décrire l'approche « polarisée » (80/20) : beaucoup de facile, un peu de dur, peu de « moyen ».
> **Mis à jour par :** personne (contenu du projet). Propose une amélioration par une pull request.

## En une phrase

Environ 80 % de ton temps de course se fait vraiment facile, les 20 % restants sont durs, et tu évites de passer tes footings dans la zone « ni facile ni dure » où l'on se fatigue sans s'en rendre compte.

## Les principes

- **Trois zones, définies par tes deux seuils** (voir `docs/glossaire.md`, « Seuils » et « Zones ») :
  - zone 1 : sous le 1er seuil. Tu peux parler en phrases complètes. C'est l'endurance fondamentale ;
  - zone 2 : entre les deux seuils. « Confortablement dur » : tempo, seuil ;
  - zone 3 : au-dessus du 2e seuil. Tu ne peux dire que quelques mots : fractionné type VMA, côtes courtes.
- **La répartition** : environ 80 % du temps en zone 1, environ 20 % en zones 2 et 3. Avec 4 à 5 séances par semaine, deux séances clés représentent 40 % des séances mais seulement 15 à 20 % du temps, échauffements compris en zone 1 : c'est le **temps** qui compte ici.
- **Le facile doit être vraiment facile.** L'erreur la plus fréquente chez les coureurs amateurs : courir les footings un peu trop vite, en zone 2. Résultat : trop fatigué pour bien réussir les séances dures, pas assez pour progresser.
- **Deux séances dures par semaine au maximum**, jamais deux jours de suite. Exemples : intervalles longs (5 × 4 min), intervalles courts (20 × 30 s / 30 s), côtes courtes (10 × 1 min).
- **Le volume progresse surtout en zone 1.** On allonge les footings et la sortie longue avant d'ajouter de l'intensité (voir `philosophie/volume-progressif.md`).
- **Récupérer fait partie du plan** : un jour de repos par semaine au minimum et une semaine allégée toutes les 3 à 4 semaines.
- **Pas un dogme.** Avant une course, la part d'allure spécifique (semi, marathon), souvent en zone 2, augmente. Beaucoup de coureurs de haut niveau ont d'ailleurs une répartition « pyramidale » (plus de zone 2 que de zone 3) : l'essentiel reste la grosse base facile.

## Une semaine type

*Exemple pour un coureur sur route à 5 séances, en phase de développement. À adapter à ton profil et à ta course.*

| Jour | Séance | But |
|---|---|---|
| Lundi | Repos | Récupérer |
| Mardi | 15 min facile, 5 × 4 min en zone 3 (récup 3 min en trottinant), 10 min facile | Développer le moteur (VO2max) |
| Mercredi | Footing 45 min en zone 1 | Du volume sans fatigue |
| Jeudi | Repos ou PPG 30 min | Renforcer, souffler |
| Vendredi | Footing 40 min en zone 1 + 6 lignes droites | Volume et foulée |
| Samedi | 15 min facile, 10 × 1 min en côte en zone 3 (récup en descendant), 10 min facile | Puissance, force |
| Dimanche | Sortie longue 1 h 15 à 1 h 45 en zone 1 | Endurance |

## Pour qui

- Les coureurs sur route, du 10 km au marathon, débutants confirmés comme expérimentés.
- Ceux qui « courent tout à la même allure » et stagnent.
- Ceux qui ont du mal à récupérer de leurs séances dures.
- Les traileurs en phase de base (on y ajoute ensuite le spécifique, voir `philosophie/trail-d-plus-specifique.md`).

## Pas pour qui / précautions

- **Reprise après blessure ou longue coupure** : pas de zone 3 au début. Suis d'abord `philosophie/retour-de-blessure.md`.
- **Débutant complet** (moins de 3 mois de course régulière) : la priorité est la régularité. La zone 3 attendra quelques semaines.
- **Zones mal réglées** : si ta FC max ou tes seuils sont des estimations, ton « facile » peut être faux. Le test de la parole et le RPE (voir glossaire) restent de bons garde-fous.
- **Chaleur, altitude, fatigue, stress** : la FC monte à effort égal. Garde l'effort facile au ressenti, quitte à ralentir beaucoup.
- **Peu de temps disponible** (moins de 3 h par semaine) : le 80/20 strict en temps peut sembler frustrant. Garder 1 à 2 séances de qualité reste raisonnable.
- **Traitement qui modifie la FC** ou problème cardiaque connu : avis médical d'abord. Les zones de FC ne sont alors plus fiables, on pilote au ressenti.

## Signaux d'alerte

- Tes footings « remontent » en zone 2 semaine après semaine, à allure égale ou plus lente.
- Deux séances dures de suite ratées ou coupées, sans raison extérieure (chaleur, sommeil court).
- FC au repos au-dessus de ta norme ou VFC en dessous, plusieurs jours d'affilée.
- Fatigue qui ne passe pas après une semaine allégée, sommeil dégradé.
- Moins d'envie : les séances dures deviennent redoutées.
- Stagnation sur 6 à 8 semaines malgré la régularité : il manque peut-être du volume ou un peu de travail au seuil.
- Une petite douleur qui revient toujours au même endroit.

## Comment le coach l'applique

- **Ce qu'il lit dans Nolio** : les séances réalisées (durée, FC, allure, D+), le RPE et tes commentaires. Il utilise **tes zones enregistrées dans Nolio** en priorité, pas des pourcentages génériques.
- **Ce qu'il calcule** : la part de temps en zone 1 et en zones 2 + 3, sur 7 et sur 28 jours, et la FC moyenne de tes footings par rapport au haut de ta zone 1.
- **Ce qu'il signale** : un footing trop rapide (« tu étais en zone 2 pendant 25 min sur 45 »), une semaine sous 70 % de facile, deux séances dures trop rapprochées.
- **Quand il construit ou adapte une semaine** : 2 séances clés au plus, séparées par au moins un jour facile ; sortie longue facile ; semaine allégée toutes les 3 à 4 semaines. Un feu orange ou rouge du matin transforme la séance dure en facile ou en repos.
- **Mode `avec-coach`** : il explique la séance prévue par ton coach (dans quelle zone, pourquoi) et la débriefe. Si la répartition dérive, il te suggère une question à poser à ton coach. Il ne propose pas de séance et n'écrit rien dans Nolio.
- **Mode `autocoache`** : il propose la semaine (`conversations/planifier.md`), te montre un récap, et ne crée les séances dans Nolio qu'après ta validation explicite.

## Sources

- Seiler K. S., Kjerland G. Ø. (2006). Quantifying training intensity distribution in elite endurance athletes: is there evidence for an "optimal" distribution? *Scandinavian Journal of Medicine & Science in Sports*, 16(1), 49–56. https://doi.org/10.1111/j.1600-0838.2004.00418.x — chez de jeunes skieurs de fond, environ 75 % des séances sous le 1er seuil.
- Seiler S. (2010). What is best practice for training intensity and duration distribution in endurance athletes? *International Journal of Sports Physiology and Performance*, 5(3), 276–291. https://doi.org/10.1123/ijspp.5.3.276 — la synthèse de référence sur le modèle à 3 zones et la répartition 80/20.
- Stöggl T., Sperlich B. (2014). Polarized training has greater impact on key endurance variables than threshold, high intensity, or high volume training. *Frontiers in Physiology*, 5, 33. https://doi.org/10.3389/fphys.2014.00033 — 9 semaines, comparaison de quatre répartitions chez des sportifs d'endurance entraînés.
- Casado A., González-Mohíno F., González-Ravé J. M., Foster C. (2022). Training periodization, methods, intensity distribution, and volume in highly trained and elite distance runners: a systematic review. *International Journal of Sports Physiology and Performance*, 17(6), 820–833. https://doi.org/10.1123/ijspp.2021-0435 — chez les coureurs de fond de haut niveau, répartition plutôt pyramidale.
- Fitzgerald M. (2014). *80/20 Running: Run Stronger and Race Faster by Training Slower*. New American Library (Penguin). https://www.penguinrandomhouse.com/books/316683/8020-running-by-matt-fitzgerald/9780451470881/ — la version grand public, avec des plans.
