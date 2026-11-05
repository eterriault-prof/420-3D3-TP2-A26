# TP2 — Refactorisation avec les patrons Composite et Stratégie
**420-3D3 · Programmation orientée objet et patrons de conception**

* Travail en équipe de 2
* Pondération : 22%

---

## Mise en contexte

**GameNeuve** est un studio de jeux vidéo fictif qui développe des jeux d'aventure et de RPG. Leur catalogue contient trois types de produits numériques :

- **Jeux** : le produit principal, vendu seul.
- **DLC** (*downloadable content*, ou extension) : un contenu supplémentaire vendu séparément qui s'ajoute à un jeu existant — un nouveau chapitre, une nouvelle région, etc. Il ne peut pas être joué sans le jeu de base.
- **Bundles** : des regroupements de produits vendus ensemble à prix réduit. Un bundle peut contenir des jeux, des DLC, ou même d'autres bundles.

L'équipe de développement a construit une première version fonctionnelle de leur site de vente en ligne. Le site affiche le catalogue, permet de trier les produits et de naviguer vers la page détail de chaque produit ou bundle.

Le code de base fonctionne — mais il est mal conçu. Votre mandat est de le **refactoriser** en introduisant le **patron Composite** et le **patron Stratégie**, sans modifier le comportement visible du site.

---

## Catalogue GameNeuve

Le fichier `data/catalogue.json` contient les produits suivants. Vous n'avez pas à le modifier.

**Jeux individuels et DLC**

| Nom | Type | Prix | Description courte |
|---|---|---|---|
| Fleuve Noir | Jeu | 24,99 $ | RPG d'exploration dans un Montréal dystopique des années 2080 |
| Fleuve Noir : Le Souterrain | DLC | 12,99 $ | Extension souterraine — tunnels et factions rivales sous la ville |
| Les Plaines | Jeu | 19,99 $ | Survie en monde ouvert dans les prairies canadiennes |
| Boréal | Jeu | 21,99 $ | Aventure narrative dans la forêt nordique québécoise |
| Boréal : Hiver Éternel | DLC | 9,99 $ | Conclusion de l'histoire de Mara dans une région enneigée |
| Citadelle | Jeu | 17,99 $ | Stratégie médiévale au tour par tour avec cartes procédurales |

**Bundles**

| Nom | Contenu | Rabais |
|---|---|---|
| Édition Complète Fleuve Noir | Fleuve Noir + Le Souterrain | 20 % |
| Édition Complète Boréal | Boréal + Hiver Éternel | 20 % |
| Pack Découverte GameNeuve | Les Plaines + Citadelle | 15 % |
| Méga Pack GameNeuve | Édition Complète Fleuve Noir + Édition Complète Boréal + Pack Découverte | 30 % |

> **Note** : Le Méga Pack contient des bundles qui contiennent eux-mêmes des produits. C'est précisément cette imbrication que le patron Composite doit gérer élégamment — et que le code de base gère avec des boucles imbriquées sur trois niveaux.

---

## Ce que vous recevez

Le dépôt GitHub contient :

```
app.py              ← frontend Flask (ne pas modifier, sauf la section balisée)
catalogue.py        ← à refactoriser
models.py           ← à refactoriser
templates/          ← ne pas modifier
static/             ← ne pas modifier
data/catalogue.json ← ne pas modifier
```

Le site tourne avec `python app.py` après avoir installé Flask (`pip install flask`).

---

## Votre mandat

Refactorisez `models.py` et `catalogue.py` en introduisant :

**Le patron Composite** pour modéliser la hiérarchie de produits :
- Une classe abstraite `Composant` qui définit le contrat commun
- Une classe abstraite `Feuille` pour les produits sans enfants
- Une classe abstraite `Composite` pour les regroupements avec enfants
- Les classes de domaine `ProduitNumerique` et `Bundle` qui en héritent

**Le patron Stratégie** pour le tri et l'affichage :
- Une hiérarchie `StrategieTri` avec au moins trois stratégies concrètes
- Une hiérarchie `StrategieAffichage` avec au moins deux stratégies concrètes
- La méthode `Catalogue.afficher_produits()` qui reçoit des *instances* de stratégies (et non des chaînes de caractères). **Attention**, la classe `Catalogue` contient deux types de stratégies distinctes (tri et affichage).

Organisez votre code en fichiers et dossiers cohérents.

---

## Contrainte principale

**Le frontend (`app.py` et les templates) doit fonctionner sans modification**, à l'exception de la section clairement balisée dans `app.py` où vous instanciez vos stratégies.

Autrement dit : si le site s'affiche correctement et que toutes les fonctionnalités marchent après votre refactorisation, c'est que vous avez respecté les contrats.

---

## Comprendre le frontend fourni

> Vous n'êtes **pas évalués** sur Flask. Cette section vous donne juste ce qu'il faut pour lire le code fourni sans le modifier.

**Flask en quatre concepts :**

**1. Une route = une URL**
```python
@app.route("/")           # quand on visite http://localhost:5000/
def index():              # cette fonction s'exécute
    ...
```

**2. Lire les paramètres de l'URL**
```python
# URL visitée : /?tri=prix&affichage=compact
tri = request.args.get("tri", "nom")        # → "prix"
affichage = request.args.get("affichage", "compact")   # → "compact"
```

**3. Envoyer des données au template HTML**
```python
return render_template("catalogue.html", produits=liste, tri_actif=tri)
# → le template peut utiliser {{ tri_actif }} et {% for p in produits %}
```

**4. La section à modifier dans `app.py`**

Après votre refactorisation, modifiez uniquement les endroits dans le fichier `app.py` indiqués dans le code pour instancier vos stratégies et les passer lors de l'appel à `catalogue.afficher_produits()`.

---

## Remise

- **Dépôt** : fork du dépôt fourni sur GitHub, travail dans des branches, fusion sur `main` avant la remise
- **Date limite** : 
    - **Groupe 02**: Dimanche 29 novembre à 23h59
    - **Groupe 01**: Lundi 30 novembre à 23h59

- **Défense orale** : en classe, ~10 minutes par équipe
    - **Groupe 02**: Lundi 30 novembre 
    - **Groupe 01**: Mardi 1er décembre

Assurez-vous que votre dépôt est propre avant la remise : pas de `__pycache__`, pas de fichiers temporaires, `.gitignore` inclus.

---

## Grille d'évaluation

### Patron Composite `/40`

| Critère | Points |
|---|---|
| `Composant` abstrait avec les bonnes méthodes abstraites | /8 |
| `Feuille` et `Composite` abstraits correctement définis | /7 |
| `ProduitNumerique` hérite de `Feuille`, implémente toutes les méthodes | /8 |
| `Bundle` hérite de `Composite`, délègue récursivement sans `isinstance` | /10 |
| Organisation en fichiers cohérente (`models/composant.py`, etc.) | /7 |

### Patron Stratégie `/35`

| Critère | Points |
|---|---|
| `StrategieTri` abstraite avec la bonne signature | /5 |
| Trois stratégies de tri concrètes correctement implémentées | /10 |
| `StrategieAffichage` abstraite avec la bonne signature | /5 |
| Deux stratégies d'affichage concrètes correctement implémentées | /10 |
| `Catalogue.afficher_produits()` reçoit des instances, délègue correctement | /5 |

### Qualité du code `/10`

| Critère | Points |
|---|---|
| Annotations de type (`-> float`, `list[Composant]`, etc.) | /4 |
| Code lisible, nommage cohérent, pas de redondance inutile | /3 |
| Dépôt propre (`.gitignore`, pas de fichiers inutiles) | /3 |

### Défense orale `/15`

| Critère | Points |
|---|---|
| Explication claire du rôle de `Composant` et pourquoi il est abstrait | /5 |
| Démonstration que `Bundle` délègue sans connaître le type concret de ses enfants | /5 |
| Explication du choix de découpage en fichiers et en classes | /5 |

**Total : /100**