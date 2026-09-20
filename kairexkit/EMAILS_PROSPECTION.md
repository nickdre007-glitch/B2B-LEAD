# KairexKit — 10 emails de prospection à froid (prêts à envoyer)

**Statut : RÉDIGÉS, NON ENVOYÉS.** Deux blocages avant envoi, détaillés en bas de page.

Objectif du message : **obtenir une réponse, pas une vente.** On demande un avis, pas un rendez-vous.
Longueur cible : sous 90 mots. Un seul call-to-action. Aucune pièce jointe.

---

## Le template de base

> **Objet :** question rapide sur vos lancements de projets
>
> Bonjour {Prénom},
>
> {Accroche personnalisée — une ligne, tirée de leur site}
>
> Je construis un système de pilotage de livraison pour agences : brief cadré,
> QA imposée, validation humaine avant mise en ligne, et un tableau qui montre
> l'état de chaque projet sans avoir à demander à l'équipe.
>
> J'ai filmé 3 minutes du mécanisme. Je cherche des fondateurs d'agence pour me
> dire si c'est utile ou si je me trompe complètement.
>
> Vous me donnez votre avis ?
>
> {Signature}

**Objets alternatifs à tester (A/B) :**
- `question rapide sur vos lancements de projets`
- `3 min — vous me dites si c'est nul ?`
- `le trou noir entre la signature et le kickoff`

---

## Les 10 messages

### 1 — Invox (invox.fr, France)
> **Objet :** question rapide sur vos lancements de projets
>
> Bonjour {Prénom},
>
> Vous pilotez du content marketing, du marketing automation et du SEO pour un même client — donc plusieurs chantiers en parallèle sur un seul compte.
>
> Je construis un système de pilotage de livraison pour agences : brief cadré, QA imposée, validation humaine avant publication, et un tableau qui montre l'état de chaque chantier sans demander à l'équipe.
>
> J'ai filmé 3 minutes du mécanisme. Je cherche des fondateurs d'agence pour me dire si c'est utile ou si je me trompe.
>
> Vous me donnez votre avis ?

### 2 — Tout Simplement Digital (toutsimplement-digital.com, France)
> **Objet :** 900 clients — comment vous tenez le suivi ?
>
> Bonjour {Prénom},
>
> Plus de 900 clients accompagnés depuis 2017. À ce volume, la question n'est plus la production — c'est de savoir où en est chaque dossier sans réunion.
>
> Je construis un système de pilotage de livraison pour agences : entrée cadrée, contrôle QA, validation humaine sur les étapes sensibles, état visible en 30 secondes.
>
> J'ai filmé 3 minutes du mécanisme. Je cherche des fondateurs d'agence pour me dire si ça tient la route.
>
> Vous me donnez votre avis ?

### 3 — Parkour3 (parkour3.com, Montréal)
> **Objet :** 3 min — vous me dites si c'est nul ?
>
> Bonjour {Prénom},
>
> Développement de sites, campagnes numériques, automatisation marketing : trois flux de livraison différents dans la même agence.
>
> Je construis un système de pilotage qui impose la même logique aux trois : brief validé avant le lancement, QA cochée par une personne nommée, validation humaine avant mise en ligne.
>
> J'ai filmé 3 minutes. Je cherche des gens qui gèrent ça au quotidien pour me dire si c'est utile ou à jeter.
>
> Vous me donnez votre avis ?

### 4 — Graphéine (grapheine.com, Paris)
> **Objet :** le trou noir entre la signature et le kickoff
>
> Bonjour {Prénom},
>
> Sur du brand strategy & design, le risque n'est pas la créa — c'est le brief à moitié rempli et les allers-retours de validation qui s'étirent.
>
> Je construis un système qui bloque le démarrage tant que le brief n'est pas complet, et qui trace chaque validation client avec sa version.
>
> J'ai filmé 3 minutes du mécanisme. Je cherche des dirigeants d'agence pour me dire si ça correspond à la réalité ou pas du tout.
>
> Vous me donnez votre avis ?

### 5 — Conversationnel (conversationnel.fr, Paris / Lyon)
> **Objet :** question rapide sur vos lancements de projets
>
> Bonjour {Prénom},
>
> Deux implantations, du community management, de l'influence, de la formation : beaucoup de fils à tenir en même temps.
>
> Je construis un système de pilotage de livraison pour agences : responsable nommé à chaque étape, contrôle QA imposé, et l'état de tous les dossiers lisible en 30 secondes.
>
> J'ai filmé 3 minutes du mécanisme. Je cherche des fondateurs d'agence pour me dire si c'est utile ou si je me trompe.
>
> Vous me donnez votre avis ?

### 6 à 10 — à compléter depuis le CSV

Même structure. Pour chaque agence, remplacer uniquement la ligne d'accroche par
**un fait tiré de leur site** (service dominant, nombre de clients, implantations,
spécialité technique). Le reste ne bouge pas.

> **Objet :** question rapide sur vos lancements de projets
>
> Bonjour {Prénom},
>
> {Une ligne factuelle tirée de leur site — jamais un compliment générique}
>
> Je construis un système de pilotage de livraison pour agences : brief cadré, QA imposée, validation humaine avant mise en ligne, et un tableau qui montre l'état de chaque projet sans avoir à demander à l'équipe.
>
> J'ai filmé 3 minutes du mécanisme. Je cherche des fondateurs d'agence pour me dire si c'est utile ou si je me trompe complètement.
>
> Vous me donnez votre avis ?

**Règle d'accroche** : si la ligne pourrait être collée dans un autre email sans
changement, elle est mauvaise. Recommence.

---

## Relance unique (J+4)

> **Objet :** Re: {objet initial}
>
> Bonjour {Prénom},
>
> Je remonte ce message une fois, puis je vous laisse tranquille.
>
> La question tient en une ligne : quand un projet démarre chez vous, qui est responsable de l'étape suivante — et est-ce écrit quelque part ?
>
> Si la réponse est « ça dépend », les 3 minutes valent le coup.

Une seule relance. Pas deux.

---

## Blocages avant envoi

**1. Aucun domaine d'envoi configuré dans Resend.**
Le compte n'a aucun domaine vérifié. Sans ça, impossible d'envoyer.
À faire : ajouter le domaine, publier les enregistrements DNS (SPF, DKIM, DMARC),
vérifier, puis chauffer l'adresse progressivement avant tout volume.
Envoyer depuis un domaine neuf sans chauffe abîme durablement la délivrabilité.

**2. Conformité prospection B2B.**
La prospection B2B par email est encadrée (RGPD + règles CNIL en France).
Les conditions généralement citées : message en rapport avec la fonction
professionnelle du destinataire, identité de l'expéditeur claire, et moyen de
refus simple dans chaque message.
**Je ne suis pas certain du détail applicable à ta situation — vérifie sur le site
de la CNIL ou auprès d'un juriste avant d'envoyer, surtout en volume.**
Les destinataires étant répartis sur FR / BE / CH / CA, les règles ne sont pas
identiques partout.

**3. Adresses non collectées.**
Le CSV exporté contient les entreprises et leurs domaines, **pas les contacts
nominatifs ni les emails**. Il faut une étape d'enrichissement contacts avant envoi.

---

## Source de la liste

Dataset : `kairexkit_agences_cibles_fr_be_ch_ca_20260920225133`
Filtres : agences pub / marketing / design, 11-50 employés, France / Belgique /
Suisse / Canada, mots-clés site « agence web », « création de site internet »,
« agence digitale », « refonte de site ».
60 lignes exportées sur 353 correspondant aux filtres.
