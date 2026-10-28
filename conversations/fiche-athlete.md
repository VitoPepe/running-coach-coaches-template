# Fiche athlète — l'interview du coach sur un athlète

> **À quoi sert ce fichier :** dresser le profil d'un athlète et l'adaptation de la philosophie du coach pour lui, en 5 à 10 min. Pré-rempli depuis Nolio, complété par le coach.
> **Mis à jour par :** contenu du projet.

**Comment la lancer** : « Fais la fiche de Julie ». L'arrivée l'enchaîne pour chaque athlète, et le radar la propose quand il repère un nouvel athlète dans Nolio.
Commande : `/nouvel-athlete <prénom nom>`.

---

Tu es l'assistant du coach. Lis `CLAUDE.md`, `coach/philosophy/` et `coach/criteres-alertes.md`.

## 0. Préparer (sans rien demander)

1. Si `athletes/<slug>/` n'existe pas : trouve l'athlète dans Nolio, crée le dossier depuis `athletes/_template/` (slug : prénom-nom, minuscules, sans accents) et ajoute sa ligne dans `athletes/index.md`.
2. **Consentement** : si `consentement` n'est pas `oui`, arrête-toi. Propose le message type de `docs/consentement-rgpd.md` et reprends quand le coach confirme.
3. **Pré-remplis depuis Nolio** (marqué « (Nolio) ») : volume des 8 à 12 dernières semaines, sports, séances types, records et temps de référence, zones et repères, compétitions à venir, notes de blessure ou de maladie.
4. Pré-remplis aussi depuis `drive-sources/athletes/<slug>/` s'il y a des documents (fiche, questionnaire, bilans).
5. Passe la fiche à `fiche: en-cours`.

## 1. L'interview (une question à la fois, 10 au maximum)

Commence par ce que Nolio montre : « Julie : 6 h par semaine, 3 séances, son meilleur semi en 1 h 38 en mars, un marathon prévu le 2027-04-11. C'est bien ça ? ». Puis :

1. **En une phrase**, comment tu la décrirais à un collègue ?
2. **L'enjeu du moment** : son problème ou son défi principal aujourd'hui ?
3. **Ses points forts**, ses « bonnes facultés » ?
4. **Ses points à travailler** ?
5. **Ses objectifs** : courses, priorités A/B/C, cibles. Propose la version SMART si l'objectif est flou.
6. **Ses temps et repères** : à confirmer ou à corriger (FC max, seuil, VMA, records).
7. **Santé** : blessures passées, zone fragile, ce qui est en cours ?
8. **Contraintes** : disponibilités, matériel, vie pro et perso ?
9. **Ta philosophie pour elle** : qu'est-ce qui change par rapport à ta méthode habituelle ? Pose la question sous forme concrète : « Avec elle, tu fais aussi 80 % facile ? Même progression de volume ? Même affûtage ? ».
10. **Pour l'assistant** : à quoi dois-je faire attention avec elle ? (sous-déclare ses douleurs, part trop vite, FC poignet peu fiable…) Un seuil d'alerte à changer pour elle ?

## 2. Écrire

- `profil.md` : toutes les sections, et les seuils propres à l'athlète dans « Points de vigilance ».
- `philosophie.md` : seulement les écarts avec la philosophie générale. S'il n'y en a pas, écris « Suit la philosophie générale ».
- `sante.md` : les faits seulement, sans diagnostic.
- `journal.md` : `- AAAA-MM-JJ [agent] fiche créée avec le coach`.
- `athletes/index.md` : phase, prochaine course, « en une phrase », `fiche: complete`.
- `etat.md` : retire l'athlète des fiches à compléter ; ajoute une alerte ou une séance clé si besoin.
- Résume la fiche en 5 lignes et demande « C'est juste ? ». Corrige, puis commit `athletes: fiche <slug>` et push sur `main`.

## 3. Ce qui manque

S'il reste des trous (un test jamais fait, des disponibilités inconnues), liste-les en fin de fiche, sous « À demander à l'athlète », sous forme de questions prêtes à envoyer. Le coach les envoie lui-même.
