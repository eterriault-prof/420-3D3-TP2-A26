from strategie.strategie_affichage import StrategieAffichage


class AffichageDetaille(StrategieAffichage):
    def afficher(self, produits: list) -> list[dict]:
        resultat = []

        for produit in produits:
            donnees = {
                "id": produit.id,
                "nom": produit.nom,
                "prix_total": produit.prix_total(),
                "image_url": produit.image_url,
                "description": produit.description,
                "nb_ventes": produit.nb_ventes,
                "est_bundle": produit.est_bundle(),
            }
            if produit.est_bundle():
                donnees["nb_items"] = produit.nb_items()
            resultat.append(donnees)

        return resultat
