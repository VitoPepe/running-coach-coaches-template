# Mise à jour depuis le modèle

> **À quoi sert ce fichier :** ramener dans le repo du coach les nouveautés du modèle public (prompts, doc, robots GitHub), sans jamais toucher à ses données ni à ses réglages.
> **Mis à jour par :** contenu du projet.

**Comment le lancer** : « Mets à jour depuis le modèle », ou `/mise-a-jour`. Le bilan mensuel le propose quand le modèle a changé.
**Prérequis** : le modèle `VitoPepe/running-coach-coaches-template` est ajouté comme deuxième repo dans la session ou le projet Claude, à côté du repo du coach (`docs/installation.md`, « Recevoir les mises à jour du modèle »). S'il ne l'est pas, essaie quand même `git fetch` sur son adresse publique ; si c'est refusé, dis au coach en une phrase comment l'ajouter, et arrête-toi.

---

Lis `CLAUDE.md` et `reglages.md`. Parle au coach sans jargon : « nouveautés du modèle », jamais « diff », « patch » ou « commit ».

## 1. Ce qui a changé

1. `git fetch https://github.com/VitoPepe/running-coach-coaches-template.git main` (ou le remote du repo modèle s'il est déjà monté dans la session). `NOUVEAU` = le commit récupéré.
2. `ANCIEN` = `version_modele` dans `reglages.md`. S'il est absent ou `_à compléter_` (repo créé avant ce réglage), prends le dernier commit du modèle antérieur au premier commit du repo du coach (`git log --before=<date du premier commit> -1 FETCH_HEAD`).
3. Si `ANCIEN` = `NOUVEAU` : « Ton repo est à jour. » Fin.
4. Résume au coach les nouveautés en 3 à 6 lignes, à partir des messages de commit du modèle (`git log ANCIEN..NOUVEAU`), et demande « Je les ajoute ? ».

## 2. Ce qu'on ne touche jamais

Ce sont les données et les choix du coach. Exclus-les du report :
`coach/`, les dossiers d'athlètes et `athletes/index.md`, `reports/`, `plan/registre-nolio.md`, `etat.md`, `automations/runs.md`, `drive-sources/sources.json` et les fichiers synchronisés.

`reglages.md` : n'ajoute que les **nouveaux champs**, avec leur valeur par défaut ; ne change aucune valeur existante.

## 3. Reporter

Après le « oui » du coach :

1. Applique les changements du modèle entre `ANCIEN` et `NOUVEAU`, hors exclusions, en fusion à trois voies, pour garder les ajustements que le coach a faits sur les prompts :
   `git diff --binary --no-renames --diff-filter=d ANCIEN NOUVEAU -- . ':!coach' ':!athletes/index.md' ':!reports' ':!plan/registre-nolio.md' ':!etat.md' ':!automations/runs.md' ':!reglages.md' ':!drive-sources/sources.json' | git apply -3`
   Les fichiers que le modèle a supprimés ou renommés ne sont pas supprimés chez le coach (`CLAUDE.md` : on ne supprime jamais) : cite-les au coach, il décide.
   Puis ajoute à la main les nouveaux champs de `reglages.md`.
2. **Conflit** (le coach et le modèle ont modifié le même passage) : garde la règle du coach (elle vient souvent de `coach/retours-agent.md`) et ajoute ce que le modèle apporte de neuf à côté. Si les deux se contredisent, montre les deux versions au coach en deux lignes et demande laquelle garder.
3. Mets `version_modele: <NOUVEAU>` dans `reglages.md`.
4. Commit `modele: mise à jour <AAAA-MM-JJ>`, push sur `main` (voir la règle Git de `CLAUDE.md`).
5. Dis au coach en 2 lignes ce qui a changé pour lui, et s'il a une action à faire (par exemple activer un nouveau workflow dans l'onglet **Actions**).
