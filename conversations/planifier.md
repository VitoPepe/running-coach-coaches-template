# Planifier — proposer et écrire des séances (niveau 5)

> **À quoi sert ce fichier :** proposer une semaine ou un bloc pour un athlète, dans la philosophie du coach adaptée à cet athlète, et l'écrire dans son calendrier Nolio seulement quand le coach dit « je valide ».
> **Mis à jour par :** contenu du projet.

**Comment le lancer** : « Prépare la semaine prochaine de Julie », « Propose un bloc de 4 semaines pour Marc avant son trail ».
Sans la permission de création dans Nolio (`reglages.md`), tu t'arrêtes à l'étape B : le coach saisit lui-même.

---

Lis `CLAUDE.md`, le dossier de l'athlète (`profil.md`, `philosophie.md`, `sante.md`, les 10 dernières lignes de `journal.md`) et `coach/philosophie/`.

## A. Proposer

- **Données** (Nolio) : le volume réalisé sur les 4 dernières semaines, et les séances déjà au calendrier sur la période.
- **Construis** en suivant, dans l'ordre : la philosophie de l'athlète, puis celle du coach (périodisation, répartition, vocabulaire de séance). Respecte les disponibilités et les contraintes du profil. Tiens compte des alertes de `etat.md` et des protocoles de `injuries/` en cours.
- **Chaque séance** : date, type (dans le vocabulaire du coach), durée, contenu structuré (échauffement, corps, retour au calme), intensité dans les zones de l'athlète, but en une phrase.
- **Cite** la règle du coach qui justifie chaque choix important (« 3 semaines de charge + 1 allégée : `coach/philosophie/periodisation.md` »).
- Une séance déjà dans Nolio et absente de `plan/registre-nolio.md` : le coach l'a écrite. Tu n'y touches pas, et tu construis autour.

## B. Le récap et la validation

```
🗓️ Julie — semaine 2026-S44 — <but> · <volume> (<+x % vs semaine passée>)
Lun : repos
Mar : 1 h — 3 × 10 min au seuil (Z3) — <but>
…
→ Réponds « je valide » pour que je crée ces <n> séances dans le Nolio de Julie, ou dis-moi ce que tu veux changer.
```

**Dans une tâche planifiée, tu t'arrêtes ici.**

## C. Écrire dans Nolio (après « je valide » du coach uniquement)

1. La validation est explicite et porte sur ce récap-là.
2. Les permissions (`reglages.md`) incluent la création. Sinon, explique comment les ajouter (`docs/nolio.md`) et arrête-toi.
3. Crée les séances une par une, dans le calendrier de l'athlète.
4. Après chaque création, ajoute une ligne à `plan/registre-nolio.md`.
5. Une création échoue : arrête-toi, dis ce qui est créé ou non, ne réessaie pas en boucle.
6. Ajoute `- AAAA-MM-JJ [agent] semaine <AAAA-Sww> écrite dans Nolio (n séances)` dans le journal de l'athlète. Commit, puis push sur `main`.

## D. Ajuster ou annuler

- Seulement les séances du registre. Récap avant/après, « je valide », puis suppression et recréation, jamais de modification. Deux lignes au registre.
- « Annule ce que tu as écrit pour Julie cette semaine » : liste, confirmation, suppression, une ligne par séance.
