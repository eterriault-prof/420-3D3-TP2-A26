import json
from models import ProduitNumerique, Bundle
from .StrategieTri.StrategieTrie import StrategieTrie
from .StrategieAffichage.StrategieAffichage import StrategieAffichage


class Catalogue:

    def __init__(self, chemin_json: str):
        self._produits: dict[int, ProduitNumerique | Bundle] = {}
        self._charger(chemin_json)

    def _charger(self, chemin: str) -> None:
        with open(chemin, encoding="utf-8") as f:
            donnees = json.load(f)

        for d in donnees:
            if d["type"] == "produit":
                produit = ProduitNumerique(
                    id=d["id"],
                    nom=d["nom"],
                    description=d["description"],
                    prix=d["prix"],
                    nb_ventes=d["nb_ventes"],
                    image_url=d["image_url"]
                )
            else:
                produit = Bundle(
                    id=d["id"],
                    nom=d["nom"],
                    description=d["description"],
                    prix=d["prix"],
                    nb_ventes=d["nb_ventes"],
                    image_url=d["image_url"],
                    rabais=d.get("rabais", 0.0)
                )
            self._produits[produit.id] = produit

        for d in donnees:
            if d["type"] == "bundle":
                bundle = self._produits[d["id"]]
                for enfant_id in d.get("enfants", []):
                    bundle.ajouter(self._produits[enfant_id])

    def tous(self) -> list:
        return list(self._produits.values())

    def obtenir(self, id: int):
        return self._produits.get(id)

    def afficher_produits(self, tri: StrategieTrie , affichage: StrategieAffichage) -> list[dict]:
        produits = self.tous()
        produits = tri.trier(produits)

        # Affichage
        resultat = affichage.afficher(produits)
        return resultat

        
