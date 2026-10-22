# Seuil « à la norvégienne »

> **À quoi sert ce fichier :** décrire l'approche centrée sur le travail au seuil, inspirée du modèle norvégien, et la version simplifiée que le coach utilise pour un coureur amateur.
> **Mis à jour par :** personne (contenu du projet). Propose une amélioration par une pull request.

## En une phrase

Beaucoup de travail juste sous ton 2e seuil, découpé en fractions et contrôlé pour ne jamais déborder, sur un fond de footings très faciles ; pour un amateur, cela devient 1 à 2 séances de seuil par semaine, pilotées au cardio et au ressenti.

## Les principes

- **Le modèle d'origine (haut niveau)** : des coureurs norvégiens ont popularisé les journées de « double seuil » (une séance de seuil le matin, une le soir, environ deux jours par semaine), plus une séance plus rapide, et tout le reste très facile. L'intensité est pilotée par la mesure du lactate dans le sang (souvent entre 2 et 4 mmol/L), sur des volumes de l'ordre de 150 à 180 km par semaine. **Ce n'est pas ce que le coach te proposera tel quel.**
- **Le seuil en fractions** : couper le travail au seuil en répétitions (par exemple 5 × 6 min, 8 × 1 000 m, 3 × 10 min) avec de courtes récupérations permet d'accumuler plus de temps au seuil, avec moins de fatigue, qu'un long bloc continu.
- **Juste sous la limite** : tu dois finir en te disant « j'aurais pu en faire une ou deux de plus ». Ressenti dur mais contrôlé, autour de 6/10 (voir « RPE » dans `docs/glossaire.md`). Si la dernière fraction est un combat, c'était trop vite.
- **La version amateur que le coach applique** : 1 à 2 séances de seuil par semaine, pas plus ; intensité contrôlée par la FC (zone 2 du modèle à 3 zones, souvent environ 82 à 87 % de la FC max, mais tes zones Nolio priment) et par le RPE, **sans mesure de lactate**.
- **Les doubles séances sont réservées** aux coureurs expérimentés à gros volume, déjà habitués à courir deux fois par jour. Pour la plupart des amateurs, le risque (fatigue, blessure) dépasse le gain.
- **Les jours faciles sont très faciles** : c'est ce qui rend le seuil répété supportable. Footings bien en zone 1, sans « rattraper » l'allure.
- **On progresse en temps, pas en vitesse** : d'abord allonger le temps cumulé au seuil (20 → 30 → 40 min par séance), une variable à la fois, avec une semaine allégée toutes les 3 à 4 semaines.

## Une semaine type

*Exemple pour un coureur amateur à 5 séances, préparation 10 km à semi-marathon. À adapter à ton profil et à ta course.*

| Jour | Séance | But |
|---|---|---|
| Lundi | Repos | Récupérer |
| Mardi | 20 min facile, 5 × 6 min au seuil (récup 1 min en trottinant), 10 min facile | Séance de seuil n° 1 |
| Mercredi | Footing 45 min très facile | Récupérer en courant |
| Jeudi | 20 min facile, 8 × 3 min au seuil (récup 1 min), 10 min facile | Séance de seuil n° 2 |
| Vendredi | Repos ou PPG 30 min | Renforcer, souffler |
| Samedi | Footing 40 min très facile + 6 lignes droites | Foulée, relâchement |
| Dimanche | Sortie longue 1 h 15 à 1 h 30 très facile | Endurance |

Toutes les 2 à 3 semaines, la séance du jeudi peut être remplacée par une séance plus rapide et courte (par exemple 10 × 1 min vite), pour garder de la vitesse.

## Pour qui

- Les coureurs sur route du 5 km au semi-marathon, et les marathoniens en phase de développement.
- Ceux qui récupèrent mal des séances VMA très intenses.
- Ceux qui aiment les séances régulières, mesurables, qu'on voit progresser.
- Les coureurs avec un cardio fiable (ceinture thoracique de préférence).

## Pas pour qui / précautions

- **Débutants** (moins d'un an de course régulière) : construis d'abord la base (voir `philosophie/volume-progressif.md`).
- **Reprise après blessure** : pas de seuil tant que la course continue facile n'est pas solide (voir `philosophie/retour-de-blessure.md`).
- **Le piège** : transformer chaque séance de seuil en course contre la montre. Le seuil dérape vite au-dessus de la limite, et l'approche perd son intérêt.
- **Cardio au poignet** : peu fiable sur des fractions courtes. Dans le doute, fie-toi au ressenti et à l'allure.
- **Mesurer son lactate soi-même** n'est pas nécessaire : les repères FC et RPE suffisent pour un amateur.
- **Objectif trail long** : le seuil peut être un complément, mais le spécifique (D+, descente, durée) reste prioritaire.

## Signaux d'alerte

- Les mêmes fractions deviennent plus dures : RPE plus haut, ou FC plus haute à allure égale.
- La FC monte au-dessus de ta cible en fin de fraction : tu étais au-dessus du seuil.
- Les footings deviennent lourds, les jambes ne « reviennent » pas entre deux séances.
- FC au repos au-dessus de ta norme ou VFC en dessous, plusieurs jours d'affilée.
- La séance de seuil devient redoutée, l'envie baisse.
- Une douleur tendineuse apparaît (tendon d'Achille, genou) : le seuil répété est aussi une charge mécanique.
- Ton allure au seuil ne bouge plus sur 6 à 8 semaines.

## Comment le coach l'applique

- **Ce qu'il lit dans Nolio** : tes zones (FC et allure), puis pour chaque séance de seuil la FC et l'allure de chaque fraction, ton RPE et tes commentaires.
- **Ce qu'il calcule** : l'écart entre la FC des fractions et ta cible, la dérive entre la première et la dernière fraction, le temps total au seuil de la semaine.
- **Comment il ajuste** : si la FC dépasse la cible en fin de fraction ou si le RPE dépasse 7, il propose de ralentir ou de raccourcir la prochaine séance. S'il progresse, il ajoute une fraction ou une minute, jamais les deux à la fois.
- **Pas de double séance** sauf si ton profil le justifie (volume, ancienneté) et après une décision notée dans `decisions/`.
- **Mode `avec-coach`** : il explique la séance de seuil prévue par ton coach, te rappelle la cible et la débriefe. Il ne propose pas de séance et n'écrit rien dans Nolio ; si quelque chose cloche, il te suggère une question à poser à ton coach.
- **Mode `autocoache`** : il propose la semaine (`conversations/planifier.md`), te montre un récap, et ne crée les séances dans Nolio qu'après ta validation explicite.

## Sources

- Bakken M. (2022). *The Norwegian model of lactate threshold training and lactate controlled approach to training*. https://www.mariusbakken.com/the-norwegian-model.html — le texte de référence, écrit par un ancien coureur norvégien de haut niveau.
- Tjelta L. I. (2016). The training of international level distance runners. *International Journal of Sports Science & Coaching*, 11(1), 122–134. https://doi.org/10.1177/1747954115624813 — volumes et nombre de séances au seuil chez les coureurs de fond de niveau international.
- Casado A., Foster C., Bakken M., Tjelta L. I. (2023). Does lactate-guided threshold interval training within a high-volume low-intensity approach represent the "next step" in the evolution of distance running training? *International Journal of Environmental Research and Public Health*, 20(5), 3782. https://doi.org/10.3390/ijerph20053782 — description du modèle et des mécanismes possibles.
- Casado A., González-Mohíno F., González-Ravé J. M., Foster C. (2022). Training periodization, methods, intensity distribution, and volume in highly trained and elite distance runners: a systematic review. *International Journal of Sports Physiology and Performance*, 17(6), 820–833. https://doi.org/10.1123/ijspp.2021-0435 — revue systématique : place du seuil dans l'entraînement des coureurs de fond.
