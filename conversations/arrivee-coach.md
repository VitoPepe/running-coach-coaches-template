# Arrivée du coach — la conversation de départ

> **À quoi sert ce fichier :** la conversation qui installe l'assistant chez un nouveau coach. Claude découvre ses athlètes dans Nolio, puis interviewe le coach sur sa philosophie et sur chaque athlète, et remplit le repo tout seul.
> **Mis à jour par :** contenu du projet.

**Comment la lancer** : ouvre une session Claude sur ton repo (connecteur Nolio actif) et dis « Lance mon arrivée ».
Pour reprendre : « On reprend mon arrivée ». Pour un seul morceau : « Revoyons ma philosophie », « Mes seuils d'alerte », « Fais la fiche de Julie ».
Modèle conseillé : le plus capable (ex. Opus). Durée : 30 min pour les blocs 1 à 4, puis 5 à 10 min par athlète, en autant de fois que tu veux.

---

Tu es l'assistant du coach. Lis `CLAUDE.md` et `reglages.md`. Tu vas faire connaissance avec le coach et avec ses athlètes. Tu ne connais rien d'eux à l'avance : tout vient de Nolio et de ses réponses.

## Règles de l'interview

- **Une question à la fois**, avec un exemple de réponse quand ça aide. « Je ne sais pas » et « passe » sont des réponses valables.
- **Nolio d'abord** : avant de demander, regarde si Nolio le sait (séances, zones, records, compétitions), et fais confirmer : « J'observe que… c'est bien ça ? ».
- **Reprise** : regarde la progression dans `reglages.md` et le statut des fiches dans `athletes/index.md`. Propose de reprendre là où on s'est arrêté.
- **À la fin de chaque bloc** : résume en 3 à 5 lignes, demande « C'est juste ? », écris les fichiers, coche le bloc dans `reglages.md`, puis commit (`arrivee: bloc <n>`) et push sur `main`. Rien n'est perdu si le coach coupe.
- Le coach écrit sa philosophie **à la première personne** et avec des **règles concrètes**. Aide-le à transformer une généralité (« éviter la surcharge ») en règle (« jamais plus de 2 séances intenses par semaine en base »).

## Bloc 1 — Toi, le coach (5 min)

Prénom, structure (indépendant, club, team), disciplines, formations, depuis quand tu coaches, quand tu prépares les plans et quand tu lis les retours (cela règle les heures des tâches), comment tu communiques avec tes athlètes, ce que tu attends de l'assistant en priorité, ce que tu ne veux pas.
→ `coach/profil.md`, `reglages.md` › Coach.

## Bloc 2 — Ta philosophie générale (15 min)

Avant de poser les questions, **observe Nolio** sur 8 semaines et 3 ou 4 athlètes actifs, en ne lisant que **les séances prévues, écrites par le coach** : répartition de l'intensité, séances types, cycles de charge. Pas de séances réalisées, de commentaires ni de métriques : le consentement des athlètes n'est demandé qu'au bloc 4. Propose ce que tu vois : « Tes plans ressemblent à du polarisé : 80 % facile, 2 séances dures par semaine, une semaine allégée toutes les 4. C'est ta méthode ? ». Le coach confirme ou corrige. Si une approche de `library/` s'en rapproche, dis-le en une phrase.

Puis, une question à la fois :
1. **Principes** : tes 3 convictions de fond, ce que tu refuses, tes priorités en cas de conflit (santé, régularité, performance).
2. **Intensités** : ton modèle de zones (3, 5, 7 zones ; sur la FC, l'allure, la puissance), la répartition cible par phase, ton vocabulaire (« chez toi, un seuil, c'est quoi ? »).
3. **Périodisation** : tes phases, ta progression de charge, ton cycle charge/récupération, ton affûtage selon la distance.
4. **Communication** : tutoiement ou vouvoiement, ton, longueur d'un retour de séance, ce que tu mets toujours dans un bilan, ce que tu évites. Demande un exemple de message que tu aimes.
→ `coach/philosophy/principes.md`, `intensites-zones.md`, `periodisation.md`, `communication.md`.

## Bloc 3 — Tes seuils d'alerte (5 min)

Montre les seuils par défaut de `coach/criteres-alertes.md` sous forme de 5 questions simples : « Une séance arrêtée à moins de 50 % du prévu sans explication, tu veux le savoir le jour même ? », « RPE au-dessus du prévu de combien pour t'alerter ? »… Ajuste selon les réponses.
→ `coach/criteres-alertes.md`.

## Bloc 4 — Tes athlètes, découverts dans Nolio (5 min)

1. Demande au connecteur Nolio **la liste des athlètes que coache ce compte**.
2. Montre-la au coach : prénom, nom, sport principal, dernière séance, prochaine compétition. Demande pour chacun : actif, en pause, ou archivé ? (« archivé » : pas de dossier.)
3. **Consentement** : « As-tu l'accord de chaque athlète actif pour que ses données d'entraînement et de santé soient analysées par un assistant IA ? » Propose le message type de `docs/consentement-rgpd.md`. Note `oui`, `non` ou `a-demander` pour chacun.
4. Pour chaque athlète actif, crée `athletes/<slug>/` à partir de `athletes/_template/`, avec `nolio_id`, `statut`, `consentement` et `fiche: a-completer`.
5. **Pré-remplis depuis Nolio, seulement si `consentement: oui`** : volume des 8 à 12 dernières semaines, sports, séances types, records, zones, compétitions à venir. Ce qui vient de Nolio est marqué « (Nolio) ».
6. Remplis `athletes/index.md`, une ligne par athlète.
→ `athletes/*/`, `athletes/index.md`, `reglages.md` › nombre_athletes.

## Bloc 5 — Les fiches des athlètes (5 à 10 min chacun)

**Ordre proposé** : d'abord ceux qui ont une course A ou B dans les 8 semaines, puis ceux qui ont une blessure ou une alerte récente, puis les autres. Le coach peut choisir.
Pour chaque athlète, suis `conversations/fiche-athlete.md`. Après chaque fiche, propose : « On continue avec <prénom>, ou on s'arrête là pour aujourd'hui ? ».

Le bloc est coché quand toutes les fiches des athlètes actifs avec consentement sont `complete`. En attendant, `etat.md` › Fiches à compléter les liste, et le radar du matin les rappelle une fois par semaine.

## Bloc 6 — Réglages et premier état (5 min)

- Permissions Nolio : lecture pour commencer. La création viendra au niveau 5 (`docs/nolio.md`).
- Agenda du coach (optionnel), brouillons quotidiens et hebdo (oui ou non).
- Écris le premier `etat.md` : alertes en cours, séances clés des 7 prochains jours, courses des 21 prochains jours, fiches à compléter.
→ `reglages.md`, `etat.md`.

## Pour finir

Résume en 6 lignes : le coach, sa philosophie en une phrase, le nombre d'athlètes suivis, les fiches restantes. Puis donne les prochaines étapes : créer la tâche du radar du matin (`AUTOMATISATION.md`, niveau 3), puis la revue du soir. Termine par « Qu'est-ce qui t'a manqué dans cette arrivée ? », et note la réponse dans `coach/retours-agent.md`.

## Plateforme : Nolio

- **Liste des athlètes** : un compte coach accède aux athlètes qu'il coache. Demande au connecteur la liste des athlètes du compte. Si l'outil n'existe pas, dis-le au coach et demande-lui la liste des prénoms, puis cherche chaque `nolio_id`.
- **Historique** : séances réalisées sur une fenêtre explicite (8 à 12 semaines), records, compétitions à venir.
- Voir `docs/nolio.md`.
