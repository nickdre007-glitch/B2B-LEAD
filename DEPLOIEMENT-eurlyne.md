# Site public Eurlyne Jeannis

**URL cible :** `https://eurlyne.kairexkit.com/`
**Domaine :** `kairexkit.com`, registrar Namecheap
**Hébergement :** Netlify — `publish = "site"`, aucun build

Ce fichier est volontairement **hors** du dossier publié (`site/`) : il ne sera
jamais servi publiquement.

---

## 1. À remplacer AVANT mise en ligne

Ouvrir `site/index.html` :

| # | Chercher | Remplacer par |
|---|----------|---------------|
| 1 | `contact@eurlyne-jeannis.com` (3 occurrences) | l'email dédié réel d'Eurlyne |
| 2 | `LINKEDIN_URL` | l'URL du profil LinkedIn (ou supprimer la ligne du footer) |
| 3 | blocs `<span class="todo">Mission type</span>` | études de cas réelles (client, contexte, résultat) |

Tant que le point 1 n'est pas fait, le lien email pointe vers une adresse
inexistante. Ne pas publier avant.

---

## 2. Créer le site Netlify

1. Netlify → **Add new site → Import an existing project** → ce dépôt.
2. Branche : `claude/admiring-planck-4yolnk`.
3. Build command : **vide**. Publish directory : **`site`** (déjà fixé par `netlify.toml`).
4. Deploy. Le site répond alors sur `https://<nom-généré>.netlify.app`.

## 3. Rattacher `eurlyne.kairexkit.com`

Netlify → **Domain management → Add a domain** → saisir `eurlyne.kairexkit.com`.

### Option retenue : Netlify DNS (nameservers)

1. Netlify affiche **4 nameservers** de la forme `dns1.p0X.nsone.net` … `dns4.p0X.nsone.net`.
   Les valeurs exactes sont propres à ta zone — **copier celles affichées**, ne pas
   les deviner.
2. Namecheap → **Domain List → Manage** (kairexkit.com) → section **Nameservers**
   → choisir **Custom DNS** → coller les 4 valeurs → enregistrer (coche verte).
3. Propagation : quelques minutes à 24 h. Netlify émet le certificat Let's Encrypt
   automatiquement une fois la délégation active.

> ⚠️ **Point d'attention.** Déléguer les nameservers confie **toute la zone
> kairexkit.com** à Netlify, pas seulement le sous-domaine. Tout enregistrement
> existant chez Namecheap — MX (email), TXT (SPF, DKIM, vérifications), racine du
> domaine, autres sous-domaines — **cesse de s'appliquer** tant qu'il n'est pas
> recréé dans Netlify DNS.
>
> Avant de basculer : Namecheap → Advanced DNS → **capture d'écran de tous les
> enregistrements**, puis les recréer dans Netlify DNS juste après la délégation.
>
> Si kairexkit.com sert déjà à autre chose (email pro, site racine), l'option 
> ci-dessous est plus sûre et suffit pour un sous-domaine.

### Alternative plus sûre : garder le DNS Namecheap

Namecheap → **Advanced DNS → Add New Record** :

| Type | Host | Value | TTL |
|------|------|-------|-----|
| CNAME | `eurlyne` | `<nom-du-site>.netlify.app` | Automatic |

Rien d'autre à changer : la zone reste chez Namecheap, l'email et la racine ne
bougent pas. Netlify détecte le CNAME et émet le certificat.

*Non vérifié dans cette session — docs.netlify.com est bloqué par le proxy réseau.
Les libellés d'interface Netlify et Namecheap peuvent avoir changé ; la logique
(nameservers délégués, ou CNAME du sous-domaine vers `*.netlify.app`) reste valable.
À confirmer sur docs.netlify.com.*

---

## 4. Formulaire de contact

Le formulaire utilise **Netlify Forms** (`data-netlify="true"`, nom `eurlyne-contact`).
Après le premier déploiement :

Netlify → **Forms → `eurlyne-contact` → Notifications → Add notification →
Email notification** → saisir **uniquement** l'adresse d'Eurlyne.

Anti-spam : champ honeypot `societe-web` (invisible, déjà câblé).

---

## 5. Règle d'isolation vis-à-vis de CyberDre

Séparation appliquée dans le code, à maintenir :

- **domaine distinct** — `eurlyne.kairexkit.com`, aucun lien avec cyberdre.co ;
- aucun lien sortant, logo, nom, slogan ou couleur CyberDre ;
- identité visuelle propre : palette os/oxyde, Fraunces + Archivo + JetBrains Mono ;
- canal de contact séparé : email dédié + formulaire Netlify dédié, destinataire unique ;
- `canonical`, `og:*` et JSON-LD pointent sur `https://eurlyne.kairexkit.com/`.

Aucun élément n'est partagé avec CyberDre.
