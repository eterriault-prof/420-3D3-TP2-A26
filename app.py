from flask import Flask, render_template, request
from catalogue import Catalogue

app = Flask(__name__)
catalogue = Catalogue("data/catalogue.json")


@app.route("/")
def index():
    tri = request.args.get("tri", "nom")
    affichage = request.args.get("affichage", "compact")

    # ===== AJOUTER DU CODE ICI POUR INSTANCIER VOS STRATÉGIES APRÈS LE REFACTORING =====

    produits = catalogue.afficher_produits(tri, affichage) # Ligne à ajuster après le refactoring

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
