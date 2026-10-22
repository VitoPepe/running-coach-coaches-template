# Critères d'alerte

> **À quoi sert ce fichier :** exemple fictif — les seuils d'alerte de Hugo, ajustés pendant son arrivée (bloc 3) à partir des valeurs par défaut. Ils classent une séance en 🔴, 🟠 ou 🟢 dans le radar et la revue du soir.
> **Mis à jour par :** la conversation d'arrivée (bloc 3), puis le coach (ici : écrit pour l'exemple). Surchargeables athlète par athlète dans « Points de vigilance » de son profil.


## 🔴 Alerte — à traiter aujourd'hui
| Critère | Règle de Hugo |
|---|---|
| Douleur / blessure | Commentaire contenant douleur, mal, tendon, genou, cheville, talon, boite, arrêt, ou une gêne notée 4/10 ou plus. Une gêne légère (3/10 ou moins) est 🟠, sauf sur une zone déjà blessée (voir les règles d'interprétation) |
| Séance interrompue | Durée réalisée < 50 % du prévu sans explication |
| RPE au-dessus du prévu | RPE ≥ prévu + 2 sur un footing ou une sortie longue (« un footing ne doit jamais sembler dur »), RPE ≥ prévu + 3 sur une séance de qualité, ou RPE ≥ 9 sur une séance d'endurance |
| Malaise / santé générale | Mentions : malade, fièvre, vertige, palpitations, essoufflement anormal |

## 🟠 Vigilance — à surveiller / en parler à l'athlète
| Critère | Règle de Hugo |
|---|---|
| Séance manquée | Séance planifiée non réalisée et non commentée |
| 2 séances manquées sur 7 j | — |
| Intensité non respectée | > 15 % du temps au-dessus de Z2 sur un footing ou une sortie longue (lignes droites exclues) |
| Dérive cardiaque | FC moyenne +8 bpm à allure équivalente vs séances similaires des 4 dernières semaines |
| Fatigue déclarée | Commentaire : fatigué, lourd, pas de jambes, mal dormi… sur 2 séances consécutives |
| Charge | Charge 7 j > 1,3 × moyenne hebdo des 4 dernières semaines (1,2 pour un débutant) |
| Gêne légère | « gêne », « tire », « sensible », 3/10 ou moins, sur une zone jamais blessée, sans drapeau rouge |
| Métriques du matin | VFC sous la marge habituelle **et** FC repos à +5 bpm, 3 matins de suite (athlètes qui les partagent) |

## 🟢 Positif — à valoriser
- Séance clé réussie (cible atteinte, RPE conforme)
- Record / progression notable
- Une première chez un débutant (plus longue sortie, première séance de qualité)

## Règles d'interprétation
- Une séance modifiée **avec** un commentaire cohérent (fatigue, météo, contrainte perso) est
  rétrogradée d'un niveau.
- Toujours croiser avec `athletes/<slug>/sante.md` : une douleur sur une zone déjà blessée monte
  d'un niveau. Pour Hugo, une gêne légère sur une zone déjà blessée est donc 🔴.
- Données capteur douteuses (FC incohérente, GPS aberrant, zones Nolio par défaut) : le signaler, ne pas alerter dessus.
- Un footing conforme ne fait l'objet d'aucune ligne (`coach/retours-agent.md`).
