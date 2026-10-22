# Nouvel athlète — consignes lues par le radar

> **À quoi sert ce fichier :** quand un athlète apparaît dans Nolio, le repérer et proposer sa fiche, sans lire ses données avant son consentement.
> **Mis à jour par :** contenu du projet.

**Déclenchement** : un athlète figure dans la liste des athlètes du compte coach dans Nolio, mais pas dans `athletes/index.md`.

## Ce que tu fais

1. Ajoute une ligne dans `athletes/index.md` : prénom, `nolio_id`, `statut: actif`, `consentement: a-demander`, `fiche: a-completer`. **Ne lis aucune de ses séances ni de ses données** à ce stade.
2. Ajoute-le dans `etat.md` › Fiches à compléter.
3. Dans le radar : « 🆕 <Prénom> est arrivé dans Nolio. On fait sa fiche ? Il faut d'abord son accord (message type dans `docs/consentement-rgpd.md`). »
4. Quand le coach confirme le consentement et dit « fais sa fiche » : `conversations/fiche-athlete.md`.

Un athlète qui disparaît de Nolio : passe-le en `statut: archive` dans l'index, et signale-le au coach. Ne supprime jamais son dossier.
