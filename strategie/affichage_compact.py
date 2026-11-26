from strategie.strategie_affichage import StrategieAffichage


class AffichageCompact(StrategieAffichage):
    def afficher(self, produits: list) -> list[dict]:
        return [
            {
                "id": produit.id,
                "nom": produit.nom,
                "prix_total": produit.prix_total(),
                "image_url": produit.image_url,
                "est_bundle": produit.est_bundle(),
            }
            for produit in produits
        ]
