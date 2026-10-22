# Bonnes pratiques : utiliser l'agent avec Nolio

> **À quoi sert ce fichier :** ce qui marche bien, et les pièges, quand on travaille avec l'assistant et Nolio.
> **Mis à jour par :** contenu du projet.

## Ce qui marche bien

- **Questions ciblées, contexte explicite** : « Analyse la sortie longue de Julie samedi au regard de
  son objectif marathon » > « Comment va Julie ? ».
- **Une fenêtre de temps à chaque demande** : l'agent ne doit pas aspirer 2 ans d'historique pour
  répondre à une question sur la semaine.
- **Le repo d'abord, Nolio ensuite** : plus `athletes/<slug>/profil.md` est à jour, meilleures sont
  les analyses. 10 min de mise à jour d'un profil valent mieux qu'un long prompt.
- **Capitaliser** : quand tu corriges l'agent (« non, chez moi une séance seuil c'est… »), reporte la
  règle dans `coach/philosophie/` pour ne plus avoir à la répéter.
- **Journal athlète** : après un échange important (blessure, changement d'objectif, vie perso qui
  impacte), fais ajouter une ligne datée dans `athletes/<slug>/journal.md`.

## Pièges

- Les métriques Nolio dépendent des capteurs : FC poignet, puissance course estimée, GPS en forêt…
  Toujours vérifier la cohérence avant de conclure.
- Un RPE manquant n'est pas un RPE bas.
- Les commentaires athlètes contiennent souvent l'info la plus importante (douleur, fatigue,
  contexte) : l'agent doit les lire systématiquement.
- Ne pas confondre « séance différente du plan » et « mauvaise séance » : une adaptation
  intelligente de l'athlète n'est pas une alerte.

## Mettre à jour la base

| Quand | Quoi |
|---|---|
| Nouvel athlète | `/nouvel-athlete` |
| Nouveau test réalisé | ajouter une ligne dans `athletes/<slug>/tests.md`, mettre à jour les zones dans `profil.md` |
| Blessure / douleur | `athletes/<slug>/sante.md` + protocole dans `injuries/` s'il n'existe pas |
| Nouvelle séance de renfo type | fichier dans `strength/<sport>/` à partir du template |
| Nouvelle conviction de coach | `coach/philosophie/` |

## Prompts utiles

- « Compare le volume des 4 dernières semaines de <athlète> à ce que prévoit `coach/philosophie/periodisation.md` pour sa phase actuelle. »
- « Prépare un message pour <athlète> sur sa semaine, ton selon `coach/philosophie/communication.md`. »
- « <athlète> signale une douleur au tendon d'Achille : quel protocole de `injuries/` s'applique, et que faut-il adapter cette semaine dans le plan ? »
- « Propose une séance de renfo de 30 min pour <athlète> (trail, phase de base, sans matériel). »
