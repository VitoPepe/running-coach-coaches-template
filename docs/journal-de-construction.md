# Journal de construction

> **À quoi sert ce fichier :** les choix, les difficultés et les bonnes pratiques notés pendant la construction du projet. C'est la matière première des deux articles Medium côté coach (`docs/article-medium-facile.md`, `docs/article-medium-complet.md`).
> **Mis à jour par :** le mainteneur du projet, au fil de l'eau. Une entrée = une idée, datée.

Légende : 🧭 choix · 🧱 difficulté · ✅ bonne pratique · 🔍 découverte

Projet jumeau : `running-coach-athletes`, le coach personnel du coureur. Les deux partagent la même structure (`automations/`, `conversations/`, niveaux d'automatisation, contrôle nocturne) et le même journal de bord.

---

## 2026-10-24 — De la base de connaissances au repo qui se remplit tout seul

### 🧭 Partir du template existant, pas d'une page blanche

Le projet reprend un premier modèle d'agent de coaching déjà utilisé : `athletes/`, `injuries/`, `strength/`, `assessments/`, la synchro Google Drive, les critères d'alerte, l'analyse de séance, le bilan de progression. Le travail a consisté à le restructurer comme son jumeau côté coureur : `automations/` pour ce qui tourne seul, `conversations/` pour ce qu'on lance en parlant.
**Pourquoi :** ces morceaux avaient déjà servi. Les deux projets parlent maintenant la même langue, et un coach peut passer de l'un à l'autre.

### 🧭 L'arrivée remplace le remplissage à la main

L'ancien modèle demandait au coach d'écrire sa philosophie dans 4 fichiers vides, puis de créer une fiche par athlète. Personne ne le fait. Désormais, le coach dit « Lance mon arrivée » :
- Claude liste ses athlètes dans Nolio et pré-remplit chaque dossier ;
- il observe ses plans pour proposer sa philosophie (« tes plans ressemblent à du polarisé… ») ;
- il interviewe le coach, une question à la fois, en reprenant là où il s'était arrêté.

**Pourquoi :** le repo doit marcher pour n'importe quel coach et n'importe quel athlète. Rien n'est écrit à l'avance, tout vient de Nolio et des réponses du coach.

### 🔍 Le connecteur officiel change la donne

Le premier modèle utilisait un serveur MCP communautaire, en lecture seule, qui ne listait pas les athlètes d'un compte coach. Le connecteur officiel de Nolio se branche sur le compte du coach et donne accès aux athlètes qu'il coache.
**Conséquence :** l'arrivée peut découvrir les athlètes toute seule, et le radar peut repérer un nouvel athlète le matin de son arrivée.

### 🧭 Une philosophie à deux étages

Le coach a une philosophie générale (`coach/philosophie/`), mais il ne l'applique pas pareil à tout le monde. Chaque athlète a un `philosophie.md` qui ne contient **que les écarts** (« footings plafonnés en FC, pas en allure »).
**Pourquoi :** c'est comme ça que les coachs pensent réellement. Écrire seulement les écarts garde les fiches courtes et lisibles.

### ✅ Pas de consentement, pas d'analyse

Un athlète n'est analysé que si `consentement: oui` dans son profil. Avant, l'assistant ne connaît que son prénom et son identifiant Nolio. Un message type explique à l'athlète ce qui est lu, par qui, et comment dire non.
**Pourquoi :** les données d'entraînement touchent à la santé, et elles passent par Claude et GitHub. C'est aussi un argument de confiance pour un coach qui veut vendre ce service.

### ✅ Trier d'abord, détailler ensuite

Le radar fait un passage léger sur tous les athlètes, avec l'index et les 24 dernières heures de Nolio. Il n'ouvre le dossier complet (profil, philosophie, santé) que pour les athlètes en alerte ou qui ont une séance clé.
**Pourquoi :** avec 30 athlètes, lire 30 dossiers chaque matin coûterait cher et noierait l'essentiel. La plupart des jours, la plupart des athlètes sont « RAS ».

### 🧭 Un niveau 1 sans repo

Le radar express est un prompt complet à coller dans une tâche planifiée, avec le seul connecteur Nolio : ni repo, ni GitHub, ni configuration.
**Pourquoi :** c'est la porte d'entrée de l'article « facile ». Un coach voit la valeur dès le lendemain matin, et passe au niveau 2 quand il constate ce que le radar express ne sait pas (une gêne au tibia, banale chez un autre, est un 🔴 chez un athlète qui sort d'une périostite).

### ✅ Jamais de message envoyé à un athlète

L'assistant prépare des brouillons dans le ton du coach (`coach/philosophie/communication.md`), et le coach les envoie lui-même.
**Pourquoi :** la relation coach-athlète est le cœur du métier. Un message envoyé en son nom, même juste, abîme la confiance.

### 🧱 La même règle d'écriture que côté coureur, avec un enjeu de plus

Au niveau 5, l'assistant écrit dans le calendrier d'**un autre** que l'utilisateur. Les trois verrous du projet coureur restent (permissions Nolio, « une tâche planifiée ne vaut pas accord », registre), et une règle s'ajoute : une séance écrite par le coach n'est jamais touchée.

### 🧭 Des seuils propres à chaque athlète

Les critères d'alerte du coach sont des valeurs par défaut. Chaque profil peut les surcharger dans « Points de vigilance » (« RPE : alerte dès +2 pour elle », « FC poignet peu fiable »).
**Pourquoi :** une même séance n'a pas le même sens chez une débutante et chez un ultra-traileur. Sans ça, le radar crie au loup.

---

## Ce qui reste à faire

- [ ] Fusionner `feat/restructuration` dans `main`, puis passer le repo en public et en template (Settings → Template repository).
- [ ] Tester le mode démo (`docs/checklist-de-test.md`, partie A) sur un vrai compte Claude.
- [ ] Vérifier avec un vrai compte coach Nolio que le connecteur liste bien les athlètes, et noter le nom de l'outil dans `docs/nolio.md`.
- [ ] Tester le radar express (niveau 1) une semaine, puis l'arrivée sur un vrai coach (avec son accord et celui de ses athlètes).
- [ ] Faire relire `docs/consentement-rgpd.md` par quelqu'un de compétent avant un usage professionnel.
- [ ] Mesurer les chiffres des articles : temps d'arrivée par athlète, faux positifs du radar, consommation.
- [ ] Rédiger les deux articles à partir de `docs/article-medium-facile.md` et `docs/article-medium-complet.md`.

### ✅ L'exemple fictif sert aussi de test

Construire le coach fictif à partir des vrais prompts a révélé quatre incohérences :
- le radar express classait toute « gêne » en 🔴 ;
- le radar complet n'avait pas de rubrique pour une course à J-14 ;
- l'arrivée lisait Nolio avant d'avoir demandé le consentement ;
- la revue du soir ne prévoyait pas de brouillon pour un écart.

Les quatre sont corrigées.
**Pourquoi c'est utile :** un exemple écrit « à la main » aurait masqué ces trous. Un exemple produit en suivant les prompts les met en évidence.
