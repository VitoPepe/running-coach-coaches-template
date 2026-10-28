# Architecture — comment l'assistant fonctionne, en schémas

> **À quoi sert ce fichier :** comprendre le système d'un coup d'œil : qui parle à qui, comment l'arrivée remplit le repo, ce qui se passe dans une journée, comment le tri garde l'assistant économe, et comment les plans restent ceux du coach.
> **Mis à jour par :** contenu du projet.

## 1. Vue d'ensemble

```mermaid
flowchart TB
    C(["🧑‍🏫 Le coach · app Claude"])
    subgraph CL["🧠 Claude, compte du coach"]
        direction LR
        T["⏰ Tâches planifiées<br/>radar · revue · bilans"]
        S["💬 Conversations<br/>arrivée · fiche · message · planifier"]
    end
    subgraph R["📁 Le repo du coach : la mémoire"]
        direction LR
        CO["coach/<br/>philosophie · seuils · ton"]
        AT["athletes/<br/>un dossier par athlète"]
        PR["automations/ · conversations/<br/>les prompts"]
    end
    N[("Nolio<br/>compte coach : tous ses athlètes")]
    GH["🔍 GitHub Action<br/>contrôle nocturne, mail si problème"]
    A(["🏃 Les athlètes"])
    C <-->|"radar, brouillons, questions"| CL
    CL <-->|"lit, écrit, commit"| R
    CL -->|"lit ; écrit seulement après « je valide »"| N
    A -->|"séances, commentaires, RPE"| N
    C -.->|"envoie lui-même les messages"| A
    R -->|"automations/runs.md, chaque nuit"| GH
```

L'assistant n'écrit **jamais** aux athlètes : il prépare des brouillons, et le coach les envoie.

## 2. L'arrivée : du compte Nolio au repo rempli

```mermaid
flowchart TD
    S(["« Lance mon arrivée »"]) --> B1["1 · Le coach<br/>profil, horaires, attentes"]
    B1 --> B2["2 · Sa philosophie<br/>observée dans Nolio, puis confirmée"]
    B2 --> B3["3 · Ses seuils d'alerte"]
    B3 --> B4["4 · Ses athlètes<br/>liste lue dans Nolio"]
    B4 --> CS{"Consentement<br/>de l'athlète ?"}
    CS -->|"oui"| PF["Dossier créé et pré-rempli<br/>depuis Nolio"]
    CS -->|"pas encore"| MIN["Prénom et nolio_id seulement<br/>message type proposé"]
    PF --> B5["5 · Fiche, athlète par athlète<br/>enjeu, forces, temps, santé,<br/>philosophie adaptée"]
    B5 --> B6["6 · Réglages et premier état"]
    MIN -.->|"quand il dit oui"| B5
```

Chaque bloc est écrit et commité dès qu'il est fini : le coach peut s'arrêter et reprendre plus tard. Un athlète qui arrive ensuite dans Nolio est repéré par le radar, qui propose sa fiche.

## 3. Une journée

```mermaid
sequenceDiagram
    autonumber
    participant At as Athlètes
    participant N as Nolio
    participant Ra as Radar 07:07
    participant C as Coach
    participant Re as Revue 20:37
    participant R as Repo
    At->>N: séances et commentaires de la veille
    Ra->>R: lit etat.md et athletes/index.md
    Ra->>N: 24 h de tous les athlètes suivis
    Ra->>R: détail seulement des athlètes en alerte
    Ra->>C: 🔴 🟠 ⭐ 🏁 🆕 en 2 minutes de lecture
    Ra->>R: rapport du jour et etat.md
    C->>At: appelle, adapte, encourage
    At->>N: séances du jour
    Re->>N: séances du jour
    Re->>C: analyses et brouillons de commentaires
    C->>N: colle les commentaires qu'il valide
    Re->>R: journaux des athlètes et etat.md
```

## 4. Trier d'abord, détailler ensuite

C'est ce qui permet de suivre 5 ou 30 athlètes sans que le coût explose.

```mermaid
flowchart LR
    ALL["Tous les athlètes suivis<br/>index + 24 h de Nolio"] --> TRI{"Tri rapide<br/>coach/criteres-alertes.md"}
    TRI -->|"RAS, conformes"| OK["une ligne :<br/>😶 RAS"]
    TRI -->|"🔴 🟠 ⭐ 🏁"| DET["Ouvre profil, philosophie,<br/>santé de CET athlète"]
    DET --> ACT["Action proposée<br/>avec sa source"]
```

## 5. Quelle philosophie s'applique

```mermaid
flowchart TD
    Q["Une décision sur un athlète"] --> A1{"athletes/slug/philosophie.md<br/>en parle ?"}
    A1 -->|"oui"| U1["On applique l'adaptation du coach pour cet athlète"]
    A1 -->|"non"| U2["On applique coach/philosophy/"]
    U2 -.->|"si le coach demande une alternative"| B["library/<br/>présentée à part, « hors philosophie du coach »"]
```

## 6. La mémoire : qui lit quoi

```mermaid
flowchart TB
    RA["📡 radar-matin"] -->|"écrit"| Q["reports/daily/AAAA-MM-JJ.md"]
    RA -->|"réécrit"| ET["etat.md<br/>mémoire courte du groupe"]
    RV["🌙 revue-soir"] -->|"ajoute"| J["athletes/slug/journal.md"]
    RV -->|"met à jour"| ET
    ET -->|"lu chaque matin"| RA
    Q -->|"les 7 radars"| BH["📊 bilan-hebdo"]
    BH -->|"écrit"| H["reports/weekly/AAAA-Sww.md"]
    H -->|"4 ou 5 bilans"| BM["🗓️ bilan-mensuel"]
    BM -->|"écrit"| M["reports/monthly/AAAA-MM.md"]
```

## 7. Le plan reste celui du coach (niveau 5)

```mermaid
sequenceDiagram
    autonumber
    participant T as Bilan du dimanche
    participant C as Coach
    participant N as Nolio
    participant R as Repo
    T->>C: « la semaine de Julie est trop chargée après sa fatigue »
    Note over T,N: la tâche s'arrête ici : elle n'écrit jamais dans Nolio
    C->>T: « propose un ajustement »
    T->>C: récap avant/après, séance par séance
    C->>T: « je valide »
    T->>N: supprime et recrée seulement ses propres séances
    T->>R: plan/registre-nolio.md
```

Trois verrous :
1. **Les permissions Nolio** : la lecture seule jusqu'au niveau 4, et jamais « modification ».
2. **La règle de `CLAUDE.md`** : jamais d'écriture pendant une tâche planifiée, et jamais sans récap ni « je valide ».
3. **Le registre** : l'assistant ne touche qu'aux séances qu'il a créées lui-même.

## 8. Le contrôle nocturne

```mermaid
sequenceDiagram
    participant T as Chaque tâche
    participant R as automations/runs.md
    participant GA as GitHub Action 04:17 UTC
    participant C as Coach
    T->>R: AAAA-MM-JJ HH:MM | radar | ok | —
    GA->>R: lit les dernières lignes
    alt tout va bien
        GA-->>GA: ✅ « Ton assistant tourne bien »
    else tâche absente, en échec, ou lien cassé
        GA->>C: mail de GitHub avec le rapport
    end
```
