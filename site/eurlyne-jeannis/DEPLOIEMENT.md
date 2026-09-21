# Page publique — Eurlyne Jeannis

Cible : `https://cyberdre.co/eurlyne-jeannis/`
Fichier unique, autonome, sans dépendance build. Seules ressources externes : Google Fonts.

---

## 1. À remplacer AVANT mise en ligne

Ouvrir `index.html` et corriger ces trois points :

| # | Chercher | Remplacer par |
|---|----------|---------------|
| 1 | `contact@eurlyne-jeannis.com` (3 occurrences) | l'email dédié réel d'Eurlyne |
| 2 | `LINKEDIN_URL` | l'URL du profil LinkedIn (ou supprimer la ligne) |
| 3 | blocs `<span class="todo">Mission type</span>` | études de cas réelles (client, contexte, résultat) |

Tant que le point 1 n'est pas fait, le lien email de la page pointe vers une adresse
qui n'existe pas. Ne pas publier avant.

---

## 2. Déploiement Netlify — option A : même site que cyberdre.co (recommandé)

Le dossier `eurlyne-jeannis/` est autonome. Le copier dans le répertoire publié du
site cyberdre.co, puis déployer normalement.

```
<publish dir de cyberdre.co>/
└── eurlyne-jeannis/
    └── index.html
```

Ne pas copier `site/_headers` si cyberdre.co possède déjà son propre `_headers` :
Netlify n'en lit qu'un seul, à la racine du publish dir. Fusionner les règles à la main
le cas échéant.

## 3. Déploiement Netlify — option B : site Netlify séparé

1. Nouveau site Netlify branché sur ce dépôt, branche `claude/admiring-planck-4yolnk`.
   `netlify.toml` fixe déjà `publish = "site"`. Aucune commande de build.
2. Dans le `_redirects` du site cyberdre.co, ajouter :

```
/eurlyne-jeannis/*  https://<nom-du-site>.netlify.app/eurlyne-jeannis/:splat  200!
```

Le statut `200!` est un rewrite : l'URL affichée reste `cyberdre.co/eurlyne-jeannis/`.

---

## 4. Formulaire de contact

Le formulaire utilise **Netlify Forms** (`data-netlify="true"`, nom `eurlyne-contact`).
Après le premier déploiement :

Netlify → Forms → `eurlyne-contact` → Notifications → Add notification → Email notification
→ saisir **uniquement** l'adresse d'Eurlyne.

Protection anti-spam : champ honeypot `societe-web` (invisible, déjà câblé).
En option B, le formulaire est détecté par le site Netlify qui héberge le HTML, pas par
cyberdre.co — les soumissions arrivent dans le dashboard du site séparé.

---

## 5. Règle d'isolation vis-à-vis de CyberDre

Contrainte appliquée dans le code, à maintenir :

- aucun lien sortant vers cyberdre.co ni vers une page CyberDre ;
- aucun logo, nom, slogan ou couleur CyberDre ;
- identité visuelle distincte : palette os/oxyde, Fraunces + Archivo + JetBrains Mono ;
- canal de contact séparé : email dédié + formulaire Netlify dédié, un seul destinataire ;
- balises `canonical`, `og:*` et JSON-LD pointant sur la personne, pas sur la marque.

La page partage le domaine, rien d'autre.
