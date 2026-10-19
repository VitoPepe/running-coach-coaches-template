# Critères d'alerte

> Valeurs par défaut **à ajuster** selon ma philosophie. Un critère peut être surchargé par athlète
> dans la section « Points de vigilance » de son `profil.md`.

## 🔴 Alerte — à traiter aujourd'hui
| Critère | Règle par défaut |
|---|---|
| Douleur / blessure | Commentaire athlète contenant un mot-clé de douleur (douleur, mal, gêne, tendon, genou, cheville, talon, boite, arrêt…) ou un mot-clé d'un protocole `injuries/` |
| Séance interrompue | Durée réalisée < 50 % du prévu sans explication |
| RPE très au-dessus du prévu | RPE ≥ prévu + 3, ou RPE ≥ 9 sur une séance d'endurance |
| Malaise / santé générale | Mentions : malade, fièvre, vertige, palpitations, essoufflement anormal |

## 🟠 Vigilance — à surveiller / en parler à l'athlète
| Critère | Règle par défaut |
|---|---|
| Séance manquée | Séance planifiée non réalisée et non commentée |
| 2 séances manquées sur 7 j | — |
| Intensité non respectée | > 15 % du temps hors zone cible sur une séance d'endurance (sur-intensification) |
| Dérive cardiaque | FC moyenne +8 bpm à allure/puissance équivalente vs séances similaires des 4 dernières semaines |
| Fatigue déclarée | Commentaire : fatigué, lourd, pas de jambes, mal dormi… sur 2 séances consécutives |
| Charge | Charge 7 j > 1,3 × moyenne hebdo des 4 dernières semaines |

## 🟢 Positif — à valoriser
- Séance clé réussie (cible atteinte, RPE conforme)
- Record / progression notable

## Règles d'interprétation
- Une séance modifiée **avec** un commentaire cohérent (fatigue, météo, contrainte perso) est
  rétrogradée d'un niveau.
- Toujours croiser avec `athletes/<slug>/sante.md` : une douleur sur une zone déjà blessée monte
  d'un niveau.
- Données capteur douteuses (FC incohérente, GPS aberrant) : le signaler, ne pas alerter dessus.
