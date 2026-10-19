# Bilan de progression

**But** : dire si un athlète progresse d'une saison à l'autre, en croisant ses courses et son
entraînement. Méthode et indicateurs : `assessments/progress-indicators.md`.

**Entrées** : un athlète (`athletes/<slug>/`) et des saisons (par défaut : toutes les années
civiles depuis le début du récap courses).

**Sortie** : `reports/progress/<slug>-AAAA-MM-JJ.md`. S'il existe déjà un rapport du jour ou
un rapport « partie 1 » récent, on le **complète** au lieu d'en créer un nouveau.

## Partie 1 — Courses (récap courses)

Source : `drive-sources/athletes/<slug>/races/course.csv`.
1. Paires de courses comparables (même course ou même profil : distance ±15 %, D+ ±20 %,
   technicité ±1) : temps, VAP, FC moyenne/max, RPE, exécution, efficacité (m/min ÷ FC moy).
2. Équivalent 10k (Riegel, exposant 1,06) pour les courses route.
3. Médianes par saison pour le trail < 35 km (en excluant les courses où la motivation
   manquait : RPE ≤ 5 et exécution ≤ 4) et pour le trail ≥ 40 km.
4. FC max atteinte en course par saison.
5. Limites récurrentes (colonnes Commentaire et Capitalisation), comptées.

## Partie 2 — Entraînement (MCP Nolio)

Prérequis : le connecteur Nolio est actif. Rester économe : fenêtres de dates explicites, un
mois à la fois pour les listes de séances, et des séries temporelles (streams) seulement pour
quelques séances choisies.

1. **Identité** : récupérer le profil Nolio. Si `nolio_id` est vide dans
   `athletes/<slug>/profil.md`, le signaler avec la valeur à recopier.
2. **Records par saison**, une fenêtre par année civile (outil de records, si disponible) :
   - allure (`par`) en distance : 1 000, 5 000, 10 000 et 21 097 m ;
   - FC (`phrr`) en durée : 60, 300 et 1 200 s. La FC soutenue maximale baisse-t-elle de saison
     en saison ? Si oui, une FC plus basse en course n'est pas forcément un gain d'efficacité.
   - le sport course à pied / trail est identifié par son ID, récupéré sur une séance.
3. **Volume mensuel** (liste des séances réalisées, mois par mois) : km, D+, heures, nombre de
   séances, par sport. À comparer au volume indiqué dans `profil.md`.
4. **Efficacité aérobie** : sur les footings faciles et plats (moins de 15 m D+/km, durée
   45-90 min, FC moyenne sous le seuil − 25 bpm), calculer la vitesse (m/min) divisée par la FC
   moyenne. Prendre la médiane par mois. Si elle monte, l'aérobie progresse.
5. **Découplage cardiaque** : pour 3 à 4 sorties longues (> 1 h 45) par saison, récupérer les
   streams et comparer le ratio vitesse/FC entre la 1re et la 2e moitié. Moins de 5 %, c'est
   bon ; s'il diminue d'une saison à l'autre, l'endurance progresse.
6. **Vitesse ascensionnelle** : sur les séances de côtes et les sorties avec plus de 40 m D+/km
   (2-3 par saison), calculer les m/h sur les montées continues de plus de 5 min, à partir de
   l'altitude dans les streams. Les comparer à FC égale.
7. **Contexte** : notes Nolio de type blessure, malade, inconfort ou repos, pour situer les
   coupures. Métriques et métadonnées (poids, sommeil, VFC) si l'API les donne ; sinon, le noter.

## Rédaction

- Ajouter au rapport une section « Partie 2 — Entraînement (Nolio) » avec un tableau par
  indicateur (saisons en colonnes), puis **mettre à jour le tableau Verdict** : confirmer,
  nuancer ou contredire la partie 1, et ajuster le niveau de confiance.
- Répondre explicitement aux questions ouvertes du profil de l'athlète. Exemple : une FC plus
  basse en course est-elle un gain d'efficacité, ou une FC bridée par la fatigue ? Si la FC
  maximale soutenue sur 5-20 min baisse alors que l'allure à FC basse progresse, ça penche vers
  « efficacité réelle, mais plafond bridé ».
- Citer les séances utilisées (date + titre Nolio) et préciser ce qui n'a pas pu être récupéré.
- Ajouter une ligne datée dans `athletes/<slug>/journal.md`.
- **Si tu n'as pas d'accès en écriture au repo** (par exemple dans un projet claude.ai), rends le
  fichier du rapport complet dans un bloc de code, prêt à être copié, plus la ligne de journal.
