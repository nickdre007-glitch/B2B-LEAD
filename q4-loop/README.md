# Loop Q4 CyberDre — Exécutant

Date : 2026-09-25. Statuts : À faire / En cours / Vérifié / Bloqué.

## Compte rendu

| Tâche | Statut | Résultat | Preuve | Blocage | Prochaine action |
|---|---|---|---|---|---|
| A1 Méthode FR | Bloqué (rédigé) | Correctif rédigé, non intégré | Aucune capture : page inaccessible | cyberdre.co bloqué par proxy réseau ; CMS inconnu ; aucun des 2 sites Wix connectés n'est cyberdre.co | Ouvrir l'accès au domaine ou fournir le CMS |
| A2 Audit Flash | Bloqué (rédigé) | Deux blocs rédigés, lien Calendly actif confirmé | Lien `calendly.com/nick-cyberdre/cyberdre-pipeline-audit` actif (API Calendly) | Même blocage site | Intégrer les blocs, tester le clic |
| A3 Formulaire | Bloqué (spécifié) | Formulaire réel identifié : Calendly « CyberDre Pipeline Audit » | API : 1 seule question libre actuelle | API Calendly sans écriture des questions | Saisie manuelle dans l'interface Calendly (6 min) |
| A4 Promesse | Bloqué (rédigé) | Texte + point de départ des 21 jours rédigés | Description Calendly contrôlée : ancienne promesse absente | Site inaccessible pour chercher l'ancienne promesse | Rechercher « 14 jours », « mûrs » sur toutes les pages |
| A5 Cibles Roumanie | En cours | 19 entreprises retenues sur 30 : déficit de 11 | `05-cibles-roumanie.csv`, 1 URL justificative par ligne | Pages non ouvertes : preuve issue du moteur de recherche uniquement | Ouvrir les 19 URL, confirmer, puis compléter |

---

## A1 — Méthode FR (`/fr/method/`)

**Avant :** non capturé (page inaccessible). Formulations à rechercher et à supprimer :
- « conversation réservée »
- « conversation qualifiée et réservée »
- « conversations réservées », « rendez-vous réservé(s) », « rendez-vous garanti(s) », « meetings booked »

**Après (remplace le passage) :**

> CyberDre transforme les signaux de marché et réglementaires en décisions commerciales documentées. Nous évaluons les comptes, identifions les interlocuteurs pertinents et préparons la prochaine action. Nous rédigeons les messages ; votre équipe mène la prise de contact.

Contrôle : aucune promesse de rendez-vous, rôle client explicite, orthographe relue.

---

## A2 — Audit Flash (`/fr/audit-flash/`)

**Bloc 1 — À qui s'adresse l'audit ?**

> Aux MSSP, fournisseurs MDR et intégrateurs cyber qui veulent structurer leur acquisition commerciale : savoir quels comptes approcher, pourquoi maintenant et avec quel décideur.

**Bloc 2 — Quels marchés servez-vous ?**

> Vous vendez à des organisations soumises à de fortes exigences de sécurité. Nous analysons vos comptes dans quatre secteurs : télécommunications, énergie et OT, banque et services financiers, industrie pharmaceutique.

**CTA sous les blocs :** « Réserver l'audit de 30 minutes » → `https://calendly.com/nick-cyberdre/cyberdre-pipeline-audit`

---

## A3 — Questions Calendly

Événement : **CyberDre Pipeline Audit** (actif, 30 min, locale EN). Question existante conservée en dernière position (optionnelle) : « Please share anything that will help prepare for our meeting. »

Chemin : Calendly → Event types → CyberDre Pipeline Audit → Booking form → Add new question.

| # | Libellé (EN, locale de l'événement) | Libellé FR | Type Calendly | Réponses | Obligatoire |
|---|---|---|---|---|---|
| 1 | Main activity? | Activité principale ? | Radio buttons | MSSP ; MDR ; Cyber integrator / intégrateur cyber ; Other / autre | Oui |
| 2 | Current pipeline sources? | Source pipeline actuelle ? | Checkboxes | Referrals ; Partners ; LinkedIn ; Email/calls ; Website/SEO ; Advertising ; Tenders ; No regular source ; Other | Oui |
| 3 | Sales team size? | Taille équipe commerciale ? | Radio buttons | 0 ; 1 ; 2–5 ; 6–10 ; 11+ | Oui |

Décision à prendre : l'événement est en anglais. Garder EN, ou libellés bilingues « EN / FR ».

Test : réserver un créneau interne, vérifier les 3 réponses dans la fiche de l'invité, puis annuler le rendez-vous. Non fait.

---

## A4 — Promesse

**Remplacer :** « 20 comptes mûrs en 14 jours » (et « comptes mûrs », « 14 jours », « 20 ripe accounts in 14 days »)

**Par :** **20 comptes évalués, documentés, 21 jours**

**Précision :**
> Chaque compte est évalué selon des critères définis et documenté avec les sources consultées, les éléments d'adéquation, les incertitudes et la prochaine action recommandée.

**Point de départ (proposition, à valider) :**
> Les 21 jours calendaires démarrent le lendemain de la séance de cadrage, une fois le segment, le marché et la liste d'exclusion validés par écrit.

**Mention à ajouter :**
> Un compte évalué n'indique ni une intention d'achat ni un rendez-vous obtenu.

Supports à contrôler : accueil, méthode, audit-flash, offres/sprint, versions EN, LinkedIn (sélection), description Calendly (déjà conforme).

---

## A5 — Cibles Roumanie

Fichier : `05-cibles-roumanie.csv` (19 lignes, séparateur `;`).

- Les 19 lignes ont chacune une URL officielle qui mentionne une offre SOC/MSSP/MDR (d'après l'index du moteur de recherche).
- **Aucune page n'a été ouverte directement** : le proxy bloque ces domaines. Statut « Vérifié » impossible.
- Implantation marquée « hypothèse » quand elle n'est pas prouvée (GMB Computers, DAF Cyber, certSIGN).

**Écartés (preuve insuffisante ou doublon) :** Cyber Smart Defence (rattaché à Stefanini, doublon groupe), Eviden Timișoara (CloudSecOps, offre MSSP locale non prouvée), Infosys Bucarest (communiqué 2019, delivery groupe), CybrOps (pas de page SOC/MDR trouvée), Zitec (source secondaire uniquement), Big 4, UTI Grup, Dendrio, Computerland, SSG (SOC de sécurité physique), Kyndryl, Asseco SEE.

**Déficit :** 11 entreprises. Aucune ligne ajoutée artificiellement. Aucun message de prospection envoyé.
