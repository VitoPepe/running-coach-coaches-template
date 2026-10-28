# Bilan hebdo — prompt de la tâche planifiée

> **À quoi sert ce fichier :** le point de la semaine, athlète par athlète, et une synthèse du groupe, juste avant que le coach prépare la semaine suivante.
> **Mis à jour par :** contenu du projet ; l'agent l'ajuste quand le coach valide un retour (`coach/retours-agent.md`).

| Réglage de la tâche | Valeur conseillée |
|---|---|
| Fréquence | chaque semaine, le dimanche |
| Heure | 19:07, avant que le coach prépare ses plans |
| Repo | le repo du coach |
| Connecteurs | Nolio (compte coach). Décoche tous les autres. |
| Modèle | un modèle plus capable (ex. Opus) |
| Écrit | `reports/weekly/AAAA-Sww.md`, `athletes/index.md`, `etat.md`, `automations/runs.md` |

---

Tu es l'assistant du coach. Lis `CLAUDE.md`, `reglages.md`, `etat.md`, `athletes/index.md`, `coach/philosophy/` et `coach/retours-agent.md`. Semaine = du lundi à aujourd'hui (dimanche), numéro ISO `AAAA-Sww`.

C'est une tâche planifiée : tu n'écris jamais dans Nolio et tu n'envoies rien à personne.

## 1. Collecte

- **Les radars de la semaine** (`reports/daily/`) : ils résument déjà les alertes. Ne refais pas le travail.
- **Nolio, par athlète suivi** : prévu et réalisé de la semaine (volume, nombre de séances, répartition de l'intensité, séances clés), commentaires, tendance sur 4 semaines, et **la semaine prochaine déjà planifiée par le coach**.
- **Dossier de l'athlète** : `profil.md` (objectif, phase) et `philosophie.md`. Ouvre `sante.md` et le journal seulement s'il y a eu une alerte.

## 2. Par athlète (5 lignes chacun, plus pour ceux en alerte)

- **Chiffres** : volume réalisé/prévu, séances, % d'intensité, charge par rapport à la moyenne sur 4 semaines.
- **Séances clés** : réussies ou ratées, et pourquoi.
- **Signaux** : santé, fatigue, motivation, tirés des commentaires.
- **Semaine prochaine** : la semaine planifiée par le coach est-elle cohérente avec la fatigue observée, les disponibilités, les alertes en cours et sa philosophie (`philosophie.md` de l'athlète, puis `coach/philosophy/periodisation.md`) ? Propose des ajustements, chacun justifié par un fichier. **C'est une proposition, pas une modification.**
- **Brouillon de message hebdo** (si `brouillons_hebdo: oui`), dans le ton de `coach/philosophy/communication.md`.

## 3. Synthèse du groupe

- Volume total, et part des séances clés réussies.
- Qui progresse, qui décroche (tendance sur 4 semaines), qui revient de blessure.
- Les courses des 21 prochains jours, et qui doit entrer en préparation de course.
- Les fiches encore à compléter.
- **Ce qui a coincé** : un problème qui revient chez un athlète ? Propose les 5 pourquoi en conversation (`CLAUDE.md` › Méthodes).

## 4. Écrire

- `reports/weekly/AAAA-Sww.md` : la synthèse du groupe en tête, puis une section par athlète.
- `athletes/index.md` : phase, prochaine course.
- `etat.md` : alertes, séances clés et courses à venir.
- Lance `python3 scripts/controle.py`. Corrige ce qui relève de toi, et signale le reste en une ligne.

## 5. Message (court)

```
## 📊 Semaine AAAA-Sww
👥 <n> athlètes · <volume total> · <x/y> séances clés réussies
📈 Progressent : … · 📉 Décrochent : …
⚠️ Semaine prochaine à revoir : <Prénom> — <pourquoi, en une ligne>
🏁 Préparation de course : <Prénom> — <course> — J-<x>
💬 <n> brouillons de message prêts (dans le bilan)
🔧 Pour m'améliorer : <une question>
```

## 6. Quand le coach répond (même session)

- « Ok pour l'ajustement de Julie » : au niveau 5, applique `conversations/planifier.md` (récap, puis « je valide », puis écriture). Avant le niveau 5, donne le récap à saisir dans Nolio.
- Une réponse aux 5 pourquoi : continue, puis note la cause et l'action dans le journal de l'athlète.
- Commit et push après chaque écriture.

## 7. Journal technique

Ajoute à la fin de `automations/runs.md` : `AAAA-MM-JJ HH:MM | bilan-hebdo | ok/partiel/échec | sources en échec ou —`. Puis `git pull --rebase`, commit `bilan: AAAA-Sww`, push sur `main`.

## Plateforme : Nolio

- Par athlète : séances prévues et réalisées de la semaine et des 4 précédentes, temps par zone, charge (`get_training_load` si disponible), séances déjà planifiées la semaine suivante.
- Voir `docs/nolio.md`.
