# Check quotidien

**But** : en 2 minutes de lecture, savoir quels athlètes nécessitent mon attention aujourd'hui.

## Entrées
- Période : les dernières 24 h (ou depuis le dernier rapport dans `bilans/quotidien/`, max 72 h)
- Athlètes : tous les dossiers `athletes/*/` avec `statut: actif`

## Étapes
1. Lister les athlètes actifs et leur `nolio_id` depuis `athletes/*/profil.md`.
2. Pour chaque athlète, via le MCP Nolio sur la période :
   - séances planifiées et séances réalisées
   - métriques clés (durée, distance, FC, allure/puissance, RPE)
   - **commentaires de l'athlète** (toujours les lire)
3. Rapprocher planifié ↔ réalisé.
4. Appliquer `coach/criteres-alertes.md`, en tenant compte de `profil.md` (points de vigilance,
   phase) et `sante.md`.
5. Pour chaque alerte 🔴, proposer une action concrète (message, adaptation du plan, protocole
   `injuries/` à ouvrir) en citant le fichier source.
6. Écrire le rapport et ajouter une ligne dans `athletes/<slug>/journal.md` pour chaque 🔴.

## Sortie : `bilans/quotidien/AAAA-MM-JJ.md`
```markdown
# Check quotidien — AAAA-MM-JJ
Période analysée : … → …  ·  Athlètes : N actifs, N avec séance

## 🔴 À traiter aujourd'hui
- **Athlète** — séance (date, titre) — constat factuel — action proposée (source : fichier)

## 🟠 À surveiller
- …

## 🟢 À valoriser
- …

## RAS
Athlète A, Athlète B…

## Données manquantes / douteuses
- …
```
Si aucune alerte : le dire en une ligne en tête du rapport.
