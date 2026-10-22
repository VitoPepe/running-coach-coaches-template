# Le coach fictif — Hugo et ses athlètes

> **À quoi sert ce fichier :** présenter l'exemple fictif complet : Hugo, coach à Annecy, ses 4 athlètes, le scénario du samedi 2026-10-24, et comment lancer la démo.
> **Mis à jour par :** contenu du projet (exemple fictif).

**Tout est inventé.** Hugo, Julie, Marc, Léo, Sophie et Paul n'existent pas ; les courses « fictives » non plus. Toute ressemblance avec des personnes réelles serait une coïncidence.

Ce dossier a deux usages :
- **une vitrine** : un repo de coach rempli, tel qu'il est après un mois d'utilisation ;
- **la source du mode démo** : avec `plateforme: demo`, les vrais prompts du projet tournent sur ces fichiers, sans compte Nolio.

## Qui est qui

**Hugo** est coach indépendant de course sur route et de trail à Annecy, diplômé d'État. Il tutoie ses athlètes, écrit des retours courts, directs et chaleureux. Sa méthode : polarisée (80 % facile, 2 séances de qualité par semaine au plus), cycles de 3 semaines de charge et 1 allégée, zones sur la FC seuil. Il coache 4 athlètes sur Nolio, un groupe volontairement petit pour que la démo reste lisible.

| Athlète | En bref | Ce que l'exemple montre |
|---|---|---|
| Julie Martin | Marathon fictif du Lac le 2027-04-11, objectif 3 h 25 | Une athlète qui court ses footings trop vite et sous-déclare sa fatigue ; un plafond de FC propre à elle |
| Marc Dubois | Ultra des Aiguilles (fictif), 75 km, le 2026-11-07 | Bon grimpeur, descendeur fragile : séance clé, préparation de course à J-14, affûtage |
| Léo Garcia | Reprise après une périostite tibiale, 10 km en moins de 42 min au printemps | Un protocole de blessure, une gêne sur une zone déjà blessée qui passe en 🔴 |
| Sophie Bernard | Débutante, 3 séances par semaine, premier semi en mars 2027 | Une fiche « en cours », reprise plus tard ; une séance manquée |
| Paul Lefèvre | Arrivé dans Nolio le 2026-10-23 | Un nouvel athlète repéré par le radar, dont les données ne sont pas lues avant son consentement |

## Le scénario du samedi 24 octobre 2026

Le repo est dans son état du vendredi 23 au soir. Le radar du samedi matin lit les séances du vendredi :
- **Léo** a écrit « petite gêne tibia gauche 3/10 en fin de séance » sur sa première course de 30 min. Pour Hugo, une gêne légère est 🟠, mais elle touche la zone de sa périostite : elle passe en 🔴. Le radar propose l'appel avec 3 questions et le retour en phase 1 du protocole.
- **Julie** a couru son footing avec 40 % du temps en Z3 (FC moyenne 151, consigne « FC < 150 »), à deux, avec un RPE de 3 : 🟠, la 3e fois en 3 semaines.
- **Sophie** a sauté le footing de jeudi sans rien dire et couru vendredi hors plan : 🟠 léger, et sa sortie longue d'aujourd'hui fait 2 jours de suite.
- **Marc** fait aujourd'hui sa dernière séance clé (2 h 30, 1 000 m de D-, travail de descente) : ⭐, et 🏁 à J-14, l'affûtage commence demain.
- **Paul** est apparu dans Nolio : 🆕, consentement à demander.

## Ce que montre chaque fichier

| Fichier | Ce qu'il montre |
|---|---|
| [nolio-simule.md](nolio-simule.md) | Les données Nolio de la démo : athlètes, séances prévues du 19 au 27 octobre, activités du 12 au 23, métriques du matin, compétitions, records |
| [reglages.md](reglages.md) | Les réglages de Hugo ; l'arrivée est faite, sauf la fiche de Sophie |
| [etat.md](etat.md) | La mémoire courte de l'assistant au soir du 23 octobre |
| [coach/profil.md](coach/profil.md), [coach/criteres-alertes.md](coach/criteres-alertes.md), [coach/retours-agent.md](coach/retours-agent.md) | Hugo, ses seuils d'alerte ajustés, ses retours sur l'assistant |
| [coach/philosophie/README.md](coach/philosophie/README.md) | Sa philosophie en 4 fichiers, à la première personne |
| [athletes/index.md](athletes/index.md) | Le tableau de bord des 4 athlètes |
| [athletes/julie-martin/profil.md](athletes/julie-martin/profil.md) | Une fiche complète ; voir aussi sa [philosophie](athletes/julie-martin/philosophie.md) et son [journal](athletes/julie-martin/journal.md) |
| [athletes/marc-dubois/philosophie.md](athletes/marc-dubois/philosophie.md) | Une philosophie adaptée : plus de descente, affûtage de 2 semaines |
| [athletes/leo-garcia/sante.md](athletes/leo-garcia/sante.md) et [injuries/periostite.md](injuries/periostite.md) | Une santé en reprise et le protocole de Hugo, validé avec un kiné (fictif) |
| [athletes/sophie-bernard/profil.md](athletes/sophie-bernard/profil.md) | Une fiche en cours, avec ses « _à compléter_ » et ses questions pour l'athlète |
| [bilans/quotidien/2026-10-23.md](bilans/quotidien/2026-10-23.md) | Le radar du vendredi 23 |
| [bilans/hebdo/2026-S42.md](bilans/hebdo/2026-S42.md) | Le bilan du dimanche 18 octobre, avec un brouillon de message par athlète |
| [automations/runs.md](automations/runs.md) | Le journal technique des tâches planifiées, avec une exécution partielle |
| [sorties/radar.md](sorties/radar.md) | Le radar complet du samedi 24 |
| [sorties/radar-express.md](sorties/radar-express.md) | Le radar express du même matin, sans repo : la comparaison avec le radar complet |
| [sorties/revue-soir.md](sorties/revue-soir.md) | La revue du soir du vendredi 23, avec les brouillons pour Léo et Julie |
| [sorties/arrivee-extrait.md](sorties/arrivee-extrait.md) | Un extrait de la conversation d'arrivée de Hugo |

Les fichiers de `sorties/` ne font pas partie d'un repo de coach : ce sont les réponses attendues de la démo, pour comparer.

## Lancer la démo

1. Dans le `reglages.md` **à la racine du repo**, mets `plateforme: demo`.
2. Ouvre une session Claude sur le repo. L'assistant lit les fichiers de ce dossier et `nolio-simule.md` ; « aujourd'hui », c'est le samedi 24 octobre 2026.
3. Essaie, dans l'ordre que tu veux :
   - « Fais le radar du matin » → à comparer avec [sorties/radar.md](sorties/radar.md) ;
   - « Fais la revue du soir du 23 octobre » → à comparer avec [sorties/revue-soir.md](sorties/revue-soir.md) ;
   - « Fais la fiche de Sophie » → l'assistant reprend sa fiche en cours et pose les questions qui manquent ;
   - « Prépare un message pour Léo » → un brouillon dans le ton de Hugo, qui propose aussi de l'appeler.
4. En mode démo, l'assistant n'écrit aucun fichier et ne fait aucun commit : il montre ce qu'il aurait écrit.
5. Pour revenir à tes vraies données, remets `plateforme: nolio`.

Les réponses varient un peu d'une session à l'autre. Les faits, eux, ne doivent pas changer : s'ils diffèrent de `nolio-simule.md`, c'est un bug à signaler.
