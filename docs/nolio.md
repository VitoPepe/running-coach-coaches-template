# Nolio — brancher ton compte coach

> **À quoi sert ce fichier :** tout ce qui est propre à Nolio : brancher le connecteur sur ton compte coach, choisir les permissions selon ton niveau, savoir ce que l'assistant lit et écrit. C'est le seul endroit (avec la section « Plateforme » de chaque automatisation) qui parle de Nolio.
> **Mis à jour par :** contenu du projet.

## Ce qu'il te faut

- Un **compte coach Nolio** (payant). Le connecteur (MCP) officiel de Nolio est réservé aux comptes payants : coach ou Premium Athlete.
- Un compte **Claude** (claude.ai), Pro ou Max pour les tâches planifiées.
- Le connecteur se branche sur **ton** compte : l'assistant voit les athlètes que tu coaches, et seulement eux. Nolio le dit ainsi : un coach n'accède qu'aux athlètes qu'il coache.
- Tu fais partie d'une team ? Elle peut limiter ce que ses coachs ont le droit de faire avec le connecteur. Vérifie ses options.

## Brancher le connecteur (5 min)

1. Dans Claude : **Réglages → Connecteurs**.
2. Ajoute **Nolio** depuis l'annuaire, ou un connecteur personnalisé avec l'adresse `https://mcp.nolio.io/mcp`.
3. Connecte-toi avec **ton compte coach** et choisis les permissions (tableau ci-dessous).
4. Vérifie dans une session : « Liste les athlètes que je coache dans Nolio ».

Pour retirer l'accès : dans Nolio (**Paramètres → MCP**) ou dans Claude (**Réglages → Connecteurs**). Pour changer les permissions, déconnecte puis reconnecte.

## Les permissions selon ton niveau

| Permission | Niveaux 1 à 4 | Niveau 5 | Pourquoi |
|---|---|---|---|
| Lecture | ✅ | ✅ | athlètes, séances, commentaires, métriques |
| Création | ❌ | ✅ | créer les séances que tu as validées |
| Suppression | ❌ | ✅ | changer une séance = la supprimer et la recréer |
| Modification | ❌ | ❌ | Nolio ne sait pas annuler une modification |

C'est une **défense en profondeur** : tant que tu n'as coché que la lecture, l'assistant ne peut pas toucher aux plans de tes athlètes, même s'il comprend mal une consigne. Au niveau 5, tout ce qu'il écrit reste annulable et tracé dans `plan/registre-nolio.md`.

Note ce que tu as coché dans `reglages.md` (`permissions_nolio`).

## Ce que l'assistant lit et écrit

| Besoin | Utilisé par | Dans Nolio |
|---|---|---|
| Liste des athlètes du compte coach | arrivée, radar (nouveaux athlètes) | les athlètes coachés |
| Séances prévues (structure, cibles, consignes) | radar, revue, bilans, planifier | le planning de chaque athlète |
| Séances réalisées (durée, distance, D+, FC, zones, allure, blocs) | radar, revue, bilans, analyse | les activités synchronisées |
| Commentaire et RPE de l'athlète | radar, revue | rattachés à la séance réalisée |
| VFC, FC repos, sommeil (si l'athlète les partage) | radar, séance clé | `list_metrics` ; clés observées `RMSSD`, `FCREPOS`, `SOMMEIL` |
| Charge et forme | bilan hebdo | `get_training_load` |
| Records, compétitions | arrivée, bilans, préparation de course | records, séances de type compétition |
| Créer ou supprimer une séance | `conversations/planifier.md`, après « je valide » | outils de création et de suppression |

Les noms d'outils ont été observés en octobre 2026 et peuvent changer : les prompts décrivent le besoin, et l'assistant cherche l'outil équivalent.

## Les règles d'écriture

- **Jamais pendant une tâche planifiée.** Une tâche propose, ta réponse en conversation valide.
- **Jamais une séance absente du registre** : si tu l'as écrite toi-même, l'assistant n'y touche pas.
- Le détail est dans `CLAUDE.md` › Le plan appartient au coach, et dans `conversations/planifier.md`.

## Limites connues

- Les données de certaines sources (Zepp, Huawei) ne passent pas toutes par le connecteur : les séances arrivent sans leurs métriques.
- Avec beaucoup d'athlètes, l'assistant les traite un par un : c'est plus lent, mais plus fiable et plus économe.

## Sources

- [Nolio — Developers (connecteur Claude, permissions)](https://www.nolio.io/en/developers/)
- [Nolio — conditions de l'API](https://www.nolio.io/en/api-terms/)
