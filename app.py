
from flask import Flask, render_template, request

from models1.catalogue import Catalogue

# Stratégies d'affichage
from models1.StrategieAffichage.compact import compact
from models1.StrategieAffichage.detaille import detaille

# Stratégies de tri
from models1.StrategieTri.strategie_nom import strategie_nom
from models1.StrategieTri.strategie_prix import strategie_prix
from models1.StrategieTri.strategie_populaire import strategie_populaire


app = Flask(__name__)
catalogue = Catalogue("data/catalogue.json")


@app.route("/")
def index():
    tri = request.args.get("tri", "nom")
    affichage = request.args.get("affichage", "compact")

   
    # Dictionnaire des stratégies de tri
    strategies_tri = {
        "nom": strategie_nom(),
        "prix": strategie_prix(),
        "popularite": strategie_populaire()
    }

    # Dictionnaire des stratégies d'affichage
    strategies_affichage = {
        "compact": compact(),
        "detaille": detaille()
    }

    # Sélection des stratégies
    tri_selectionne = strategies_tri.get(tri, strategies_tri["nom"])

    affichage_selectionne = strategies_affichage.get(
        affichage,
        strategies_affichage["compact"]
    )

    # Transmission des stratégies au catalogue
    produits = catalogue.afficher_produits(
        tri_selectionne,
        affichage_selectionne
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
