# Installation pas à pas : GitHub, puis Claude

> **À quoi sert ce fichier :** installer l'assistant de zéro, sans rien connaître à l'informatique : d'abord ce qu'on fait sur GitHub, ensuite ce qu'on fait sur Claude, chaque clic expliqué.
> **Mis à jour par :** contenu du projet.

## Avant de commencer

**Compte environ 1 h 15** : 15 minutes sur GitHub, puis 1 h sur Claude, dont 30 minutes de première conversation avec l'assistant. Tu peux t'arrêter entre deux étapes et reprendre plus tard.

**Il te faut :**
- un ordinateur (c'est plus simple qu'un téléphone pour l'installation ; ensuite, le téléphone suffit) ;
- un abonnement **Claude Pro ou Max** sur [claude.ai](https://claude.ai) ;
- un **compte coach Nolio** (payant) et son mot de passe ;
- une adresse mail pour créer un compte **GitHub** (gratuit).

**Les deux outils, en une phrase chacun :**
- **GitHub** est un site qui garde un dossier de fichiers en ligne, avec l'historique de chaque modification. C'est **la mémoire** de ton assistant : ta philosophie, tes athlètes, ses rapports. Tu n'as rien à programmer, tu crées juste ce dossier (on dit un « repo »).
- **Claude** est **le cerveau** : il lit ce dossier, lit Nolio, et te répond. C'est aussi lui qui lance les tâches automatiques du matin et du soir.

**L'ordre compte :** fais d'abord toute la partie GitHub, puis toute la partie Claude. Claude a besoin que ton repo existe pour s'y brancher.

> 💡 GitHub est en anglais. Les noms des boutons sont écrits ici **en gras, tels qu'ils apparaissent à l'écran**, avec leur sens en français.

---

## Partie 1 · Sur GitHub (15 min)

À la fin de cette partie, tu as **ta propre copie privée** du projet sur GitHub.

### Étape 1 · Créer ton compte GitHub (5 min)

Tu as déjà un compte ? Passe à l'étape 2.

1. Va sur [github.com/signup](https://github.com/signup).
2. Saisis ton adresse mail, un mot de passe et un nom d'utilisateur (par exemple `prenom-nom-coach`). Clique sur **Continue** (continuer) à chaque fois.
3. Résous la petite vérification « je ne suis pas un robot », puis colle le **code reçu par mail**.
4. Si GitHub te pose des questions (« combien de personnes dans ton équipe ? »), tu peux répondre n'importe quoi ou cliquer sur **Skip** (passer). Choisis l'offre **Free** (gratuite) si on te la propose.
5. GitHub va te demander d'activer la **double authentification** (*two-factor authentication*). Accepte : c'est ce qui protège les données de tes athlètes. Le plus simple est l'application d'authentification de ton téléphone, ou une clé d'accès (*passkey*). **Garde les codes de secours** qu'il te donne (une photo ou un fichier rangé en lieu sûr).

✅ **Ça a marché si** tu vois ta page d'accueil GitHub, avec ta photo (ou un rond de couleur) en haut à droite.

### Étape 2 · Copier le modèle dans ton compte (2 min)

1. Ouvre la page du modèle : [github.com/VitoPepe/running-coach-coaches-template](https://github.com/VitoPepe/running-coach-coaches-template).
2. En haut à droite de la liste des fichiers, clique sur le bouton vert **Use this template** (utiliser ce modèle), puis sur **Create a new repository** (créer un nouveau repo).
3. Remplis la page :
   - **Owner** (propriétaire) : ton nom d'utilisateur, déjà choisi.
   - **Repository name** (nom du repo) : par exemple `assistant-coach`. Pas d'espace ni d'accent.
   - **Description** : laisse vide.
   - Coche **Private** (privé). **C'est obligatoire** : ton repo contiendra des données de santé de tes athlètes. Ne choisis jamais **Public**.
   - **Include all branches** : laisse décoché.
4. Clique sur **Create repository** (créer le repo). Attends quelques secondes.

✅ **Ça a marché si** tu arrives sur une page qui s'appelle `ton-nom/assistant-coach`, avec un petit cadenas et le mot **Private** à côté du nom, et la liste des fichiers (`CLAUDE.md`, `README.md`, `athletes`…).

> ❓ **Pourquoi pas « Fork » ?** Un *fork* reste relié au projet public et ne peut pas être privé. **Use this template** crée une copie indépendante et privée : c'est ce qu'il te faut.

### Étape 3 · Allumer le contrôle nocturne (2 min)

Ton repo contient deux petits robots. Le premier vérifie chaque nuit que l'assistant a bien tourné, et t'envoie un mail sinon. Le second ramène sur `main` tout ce que Claude a écrit sur une branche à part (`claude/…`), pour que tu n'aies jamais rien à fusionner toi-même. Il faut les allumer une fois.

1. Sur la page de ton repo, clique sur l'onglet **Actions** (en haut, à côté de **Code**).
2. Si GitHub affiche **I understand my workflows, go ahead and enable them** (j'ai compris, active-les), clique dessus.
3. Dans la colonne de gauche, clique sur **Contrôle de l'assistant**, puis à droite sur **Run workflow** → **Run workflow**.

✅ **Ça a marché si** une ligne apparaît dans la liste au bout d'une minute. Une croix rouge est normale à ce stade : l'assistant n'a encore rien fait. Elle passera au vert après quelques jours de tâches planifiées.

> Tu peux aussi faire cette étape à la fin. Le contrôle ne sert qu'une fois les tâches planifiées en place (partie 2, étape 7).

### Bon à savoir · modifier un fichier sur GitHub

Tu n'en as pas besoin tout de suite : l'assistant écrit lui-même ses fichiers. Mais c'est utile pour changer un réglage à la main.

1. Dans ton repo, clique sur le fichier (par exemple `reglages.md`).
2. Clique sur le **crayon** ✏️ en haut à droite du contenu (**Edit this file**).
3. Modifie le texte.
4. Clique sur le bouton vert **Commit changes…** (enregistrer), puis à nouveau sur **Commit changes** dans la fenêtre qui s'ouvre. Laisse coché **Commit directly to the main branch**.

✅ **Ta partie GitHub est finie.** Garde l'onglet ouvert, tu en auras besoin à l'étape 5.

---

## Partie 2 · Sur Claude (1 h)

À la fin de cette partie, Claude **lit ton repo et Nolio**, te connaît, et t'envoie un radar chaque matin.

> 💡 Claude a deux espaces : la **conversation** classique, et **Code** (sur [claude.ai/code](https://claude.ai/code), ou l'onglet **Code** de l'app). C'est **Code** qui sait lire et écrire dans ton repo. Malgré son nom, tu n'y écris aucun code : tu lui parles comme d'habitude.

### Étape 4 · Brancher Nolio dans Claude (5 min)

1. Sur [claude.ai](https://claude.ai), clique sur ton nom en bas à gauche → **Réglages** (*Settings*) → **Connecteurs** (*Connectors*).
2. Cherche **Nolio** dans l'annuaire et clique sur **Connecter**. Tu ne le trouves pas ? Clique sur **Ajouter un connecteur personnalisé** (*Add custom connector*), nomme-le `Nolio` et colle l'adresse `https://mcp.nolio.io/mcp`.
3. Une page Nolio s'ouvre : connecte-toi avec **ton compte coach** (pas un compte athlète).
4. Nolio te demande quelles permissions donner. Coche **Lecture** seulement. La création viendra plus tard, au niveau 5 (voir [docs/nolio.md](nolio.md)).

✅ **Ça a marché si** Nolio apparaît dans la liste des connecteurs avec l'état **Connecté**. Pour vérifier, ouvre une conversation et demande : « Liste les athlètes que je coache dans Nolio ».

### Étape 5 · Relier Claude à ton repo GitHub (5 min)

1. Va sur [claude.ai/code](https://claude.ai/code).
2. Claude propose de **connecter GitHub**. Accepte. Une page GitHub s'ouvre : connecte-toi si besoin, puis clique sur **Authorize** (autoriser).
3. GitHub te propose ensuite d'**installer l'application Claude** sur ton compte. À la question « à quels repos ? » :
   - choisis **Only select repositories** (seulement certains repos) ;
   - dans la liste **Select repositories**, coche ton repo (`assistant-coach`) ;
   - clique sur **Install** (installer).
4. Tu reviens sur Claude.

✅ **Ça a marché si**, sur [claude.ai/code](https://claude.ai/code), ton repo apparaît quand tu cliques sur le choix du repo (sous la zone où l'on écrit).

**Ton repo n'apparaît pas ?** C'est presque toujours que l'application Claude n'y a pas accès. Sur GitHub : ta photo en haut à droite → **Settings** → **Applications** (colonne de gauche) → **Installed GitHub Apps** → **Claude** → **Configure** → dans **Repository access**, ajoute ton repo → **Save**. Reviens sur Claude et recharge la page.

### Étape 6 · Ta première conversation avec l'assistant (30 min)

Compte 30 minutes, puis 5 à 10 minutes par athlète, à faire en plusieurs fois si tu veux.

1. Sur [claude.ai/code](https://claude.ai/code), choisis **ton repo** dans la liste.
2. Vérifie que **Nolio est actif** pour cette session (icône des outils ou des connecteurs, sous la zone d'écriture).
3. Écris **Lance mon arrivée** et envoie.
4. Réponds à ses questions, une à la fois. Il commence par toi, puis lit tes plans dans Nolio et te propose ta philosophie, règle tes seuils d'alerte, liste tes athlètes et fait leurs fiches avec toi.

Tu peux t'arrêter quand tu veux. Pour reprendre, ouvre une nouvelle session sur ton repo et écris **On reprend mon arrivée**.

✅ **Ça a marché si**, sur GitHub, ton repo contient maintenant un dossier par athlète dans `athletes/`, et `reglages.md` porte ton prénom.

> 🧪 **Tu veux d'abord essayer sans tes vrais athlètes ?** Sur GitHub, modifie `reglages.md` (voir « Bon à savoir » de la partie 1) : remplace `plateforme: nolio` par `plateforme: demo`. Ouvre une session et écris « Fais le radar du matin » : l'assistant travaille sur un coach fictif. Remets `plateforme: nolio` avant ton arrivée.

### Étape 7 · Les tâches automatiques du matin et du soir (20 min)

C'est ce qui fait tourner l'assistant tout seul. Tu crées 4 tâches planifiées, une seule fois.

1. Va sur [claude.ai/code/routines](https://claude.ai/code/routines) (ou onglet **Code** → **Planifiées**), puis **Nouvelle tâche**.
2. Remplis les champs :
   - **Nom** : « Assistant — radar du matin ».
   - **Prompt** : copie le texte ci-dessous tel quel.
   - **Repo** : ton repo.
   - **Connecteurs** : **Nolio seulement**. Décoche les autres (Gmail, Agenda…), ça allège chaque exécution.
   - **Fréquence** : tous les jours, 07:07.
   - **Modèle** : celui du tableau plus bas.
   - Si tu vois une option pour autoriser l'envoi sur toutes les branches (*Allow unrestricted branch pushes*), coche-la : les rapports arrivent alors directement sur `main`. Sinon, pas d'inquiétude : ils partent sur une branche `claude/…` et le robot « Fusion automatique sur main » les ramène sur `main` dans la minute.
3. Enregistre, puis clique sur **Exécuter maintenant** (*Run now*) pour tester.

```text
Lis CLAUDE.md, puis exécute le prompt du fichier automations/radar-matin.md (tout ce qui suit la ligne ---).
Date du jour : aujourd'hui, dans le fuseau de reglages.md.
C'est une tâche planifiée : n'écris jamais dans Nolio et n'envoie rien à personne.
Termine par un commit et un push sur main.
```

Recommence pour les 3 autres tâches, en changeant **le nom du fichier** dans la première ligne du prompt :

| Nom | Fichier à mettre dans le prompt | Quand | Modèle |
|---|---|---|---|
| Assistant — radar du matin | `automations/radar-matin.md` | tous les jours, 07:07 | rapide (Sonnet) |
| Assistant — revue du soir | `automations/revue-soir.md` | tous les jours, 20:37 | rapide (Sonnet) |
| Assistant — bilan hebdo | `automations/bilan-hebdo.md` | le dimanche, 19:07 | capable (Opus) |
| Assistant — bilan mensuel | `automations/bilan-mensuel.md` | le 1er du mois, 08:07 | capable (Opus) |

✅ **Ça a marché si**, quelques minutes après **Exécuter maintenant** :
- le radar s'affiche dans la session de la tâche (onglet **Code**) ;
- sur GitHub, un nouveau fichier est apparu dans `reports/daily/` ;
- `automations/runs.md` a une nouvelle ligne `ok`.

**Au quotidien**, chaque exécution apparaît comme une session dans l'onglet **Code** de l'app Claude, sur ton téléphone aussi. Tu peux y répondre directement : « Fais la fiche de Paul », « Raccourcis le brouillon pour Julie ».

---

## Partie 3 · Récapitulatif

| Où | Quoi | Une seule fois ? |
|---|---|---|
| GitHub | créer ton compte, avec la double authentification | oui |
| GitHub | **Use this template** → repo **Private** | oui |
| GitHub | onglet **Actions** → activer → **Run workflow** | oui |
| Claude | **Réglages → Connecteurs** → Nolio, compte coach, **lecture** | oui |
| Claude | [claude.ai/code](https://claude.ai/code) → connecter GitHub → app Claude sur ton repo | oui |
| Claude | session sur ton repo → « Lance mon arrivée » | puis « On reprend mon arrivée » |
| Claude | 4 tâches planifiées avec le prompt talon | oui |
| Claude | ajouter le modèle comme deuxième repo, puis « Mets à jour depuis le modèle » | une fois, puis quand le bilan mensuel le propose |

Pour aller plus loin (le niveau 5 qui écrit dans Nolio, tes Google Sheets) : [AUTOMATISATION.md](../AUTOMATISATION.md).

## Recevoir les mises à jour du modèle

Ton repo est une copie indépendante : GitHub ne lui envoie pas les améliorations faites ensuite dans le modèle. C'est l'assistant qui les ramène, sans toucher à tes athlètes, à tes réglages ni à tes rapports.

1. **Une seule fois** : dans Claude, là où tu as choisi ton repo (les réglages de ton projet ou de ta session, onglet **Code**), ajoute aussi le modèle comme deuxième repo : `VitoPepe/running-coach-coaches-template`. Il est public : rien à installer côté GitHub.
2. **Quand tu veux** : ouvre une session sur ton repo et dis **Mets à jour depuis le modèle** (ou `/mise-a-jour`). L'assistant te résume les nouveautés, attend ton « oui », les reporte, et garde les ajustements que tu as déjà faits sur ses prompts.
3. **Tu n'as pas à surveiller** : le bilan du 1er du mois te prévient en une ligne quand le modèle a des nouveautés.

✅ **Ça a marché si** `reglages.md` contient une ligne `version_modele:` remplie, et que l'assistant te dit ce qui a changé pour toi.

## Quand ça coince

| Ce que tu vois | Pourquoi | Que faire |
|---|---|---|
| Pas de bouton **Use this template** | tu n'es pas sur la page du modèle, ou pas connecté à GitHub | connecte-toi, puis rouvre le lien de l'étape 2 |
| Ton repo n'apparaît pas dans Claude | l'application Claude n'a pas accès à ce repo | étape 5, encadré « Ton repo n'apparaît pas ? » |
| « Je ne vois pas tes athlètes » | Nolio branché avec un compte athlète, ou décoché dans la session ou la tâche | reconnecte Nolio avec ton compte coach (étape 4) et vérifie qu'il est coché |
| Le radar s'affiche mais rien n'arrive dans `reports/` sur GitHub | les rapports sont sur une branche `claude/…` et le robot de fusion n'a pas tourné | onglet **Actions** : vérifie que les workflows sont activés (étape 3), puis **Fusion automatique sur main** → **Run workflow** |
| Le radar dit « une sauvegarde n'a pas pu rejoindre main » | Claude a modifié les mêmes lignes à deux endroits et n'a pas su trancher seul | réponds « règle la fusion » dans la session du radar |
| Mail « Contrôle de l'assistant » en échec | une tâche n'a pas tourné, ou un lien est cassé | le mail contient le détail ; c'est normal les premiers jours |
| L'assistant refuse d'écrire dans Nolio | il est en lecture seule, c'est voulu | voir le niveau 5 dans [AUTOMATISATION.md](../AUTOMATISATION.md) |

Pour vérifier que tout marche de bout en bout : [docs/checklist-de-test.md](checklist-de-test.md).
