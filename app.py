from flask import Flask, render_template, request
from catalogue import Catalogue

from Affichage.Afficher_Compact import Afficher_Compact
from Affichage.Afficher_Détaillé import Afficher_Détaillé

from Trier.Trier_Nom import Trier_Nom
from Trier.Trier_Prix import Trier_Prix
from Trier.Trier_Popularité import Trier_Popularité

app = Flask(__name__)
catalogue = Catalogue("data/catalogue.json")


@app.route("/")
def index():
    tri = request.args.get("tri", "nom")
    affichage = request.args.get("affichage", "compact")

    # ===== AJOUTER DU CODE ICI POUR INSTANCIER VOS STRATÉGIES APRÈS LE REFACTORING =====
    # Choisir la stratégie de tri
    if tri == "prix":
        strategie_tri = Trier_Prix()

    elif tri == "popularite":
        strategie_tri = Trier_Popularité()

    else:
        strategie_tri = Trier_Nom()


    if affichage == "detaille":
        strategie_affichage = Afficher_Détaillé()

    else:
        strategie_affichage = Afficher_Compact()


    produits = catalogue.afficher_produits(
        strategie_tri,
        strategie_affichage
    )

    return render_template(
        "catalogue.html",
        produits=produits,
        tri_actif=tri,
        affichage_actif=affichage,
    )

    

    


@app.route("/produit/<int:id>")
def detail(id: int):
    produit = catalogue.obtenir(id)
    if produit is None:
        return "Produit introuvable", 404

    return render_template("produit.html", produit=produit)


if __name__ == "__main__":
    app.run(debug=True)
