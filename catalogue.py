import json

from Trier.Trier_Nom import Trier_Nom
from Trier.StrategieTrier import StrategieTri

from Affichage.Afficher_Compact import Afficher_Compact
from Affichage.StrategieAffichage import StrategieAffichage

from models import Composant, ProduitNumerique, Bundle

class Catalogue:

    def __init__(self, chemin_json: str):
        self._produits: dict[int, Composant] = {}
        self._charger(chemin_json)
        self._strategie_tri: StrategieTri = Trier_Nom()  # Valeur par défaut
        self._strategie_affichage: StrategieAffichage = Afficher_Compact()  # Valeur par défaut

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

    

    def afficher_produits(self,tri: StrategieTri,affichage: StrategieAffichage) -> list[dict]:
        produits = self.tous()
        produits_tries = tri.trier(produits)

        return affichage.afficher(produits_tries)
