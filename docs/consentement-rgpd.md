# Consentement et données des athlètes

> **À quoi sert ce fichier :** ce qu'il faut faire avant que l'assistant analyse les données d'un athlète : l'informer, obtenir son accord, limiter les données, savoir tout supprimer. Avec un message type à lui envoyer.
> **Mis à jour par :** contenu du projet.

⚠️ **Ce n'est pas un conseil juridique.** Ce sont des bonnes pratiques de base. Si tu en fais une activité professionnelle, fais valider ta démarche, par exemple auprès de la CNIL ou d'un juriste.

## Pourquoi c'est important

- Les données d'entraînement d'un athlète (FC, VFC, sommeil, douleurs, blessures) touchent à sa **santé**. Ce sont des données sensibles, qui demandent en général un **consentement explicite**.
- Avec l'assistant, ces données passent par d'autres services : **Claude** (Anthropic) qui les analyse, **GitHub** qui stocke le repo, et **Nolio** qui les a déjà. L'athlète doit le savoir.

## Les 6 règles du projet

1. **Pas de consentement, pas d'analyse.** Le champ `consentement` du profil de l'athlète doit valoir `oui`. Sinon, l'assistant ne lit ni ses séances ni ses données, et n'écrit que son prénom et son `nolio_id`.
2. **Informer avant de demander** : quelles données, pour quoi faire, quels services, combien de temps, comment retirer son accord. Le message type ci-dessous le fait.
3. **Le moins de données possible** : seulement ce qui sert l'entraînement. Pas d'adresse, pas de numéro de sécurité sociale, pas de dossier médical : des faits utiles (« périostite tibia gauche en 2025, 6 semaines d'arrêt »).
4. **Repo privé, toujours.** Personne d'autre que toi n'y a accès.
5. **Pas de secret dans le repo** : les liens vers des documents Drive vont dans les secrets GitHub (`drive-sources/README.md`).
6. **Retrait à tout moment** : l'athlète dit non, et tu effaces (voir plus bas).

## Message type à envoyer à un athlète

> Salut <Prénom> ! J'utilise maintenant un assistant (Claude, d'Anthropic) pour mieux suivre tes séances : il lit chaque jour tes séances et tes commentaires dans Nolio, et m'aide à repérer une fatigue ou une douleur plus vite, et à préparer mes retours. C'est moi qui décide et qui t'écris, toujours.
>
> Concrètement, il voit tes séances, tes commentaires, ton RPE, et, si tu les partages, ta VFC, ta FC de repos et ton sommeil. Je garde une fiche sur toi (objectifs, repères, blessures passées) dans un espace privé (GitHub), qui n'est accessible qu'à moi.
>
> Tu es d'accord ? Tu peux changer d'avis quand tu veux : je supprime alors ta fiche, et l'assistant ne regarde plus tes données.

Note la réponse dans le profil (`consentement: oui` ou `non`) et une ligne dans son journal : `- AAAA-MM-JJ [coach] consentement : oui (message du AAAA-MM-JJ)`.

## Quand un athlète retire son accord, ou s'en va

1. Dans `athletes/<slug>/profil.md` : `consentement: non`, `statut: archive`. Dès lors, l'assistant ne lit plus ses données.
2. Supprime son dossier (`athletes/<slug>/`) et sa ligne de `athletes/index.md`, ou demande-le à l'assistant. C'est la seule suppression qu'il fait, et seulement sur ta demande explicite.
3. **L'historique Git garde une copie** des anciens fichiers. Pour un effacement complet, il faut réécrire l'historique, ou recréer le repo sans lui. Demande de l'aide si besoin.
4. Vérifie aussi `drive-sources/athletes/<slug>/` et tes Google Sheets.

## Côté Claude

- Regarde les réglages de confidentialité de ton compte Claude, notamment l'utilisation des conversations pour l'entraînement des modèles.
- Pour une activité professionnelle, regarde les offres et conditions adaptées (Claude Team ou Enterprise), et leurs engagements sur les données.
