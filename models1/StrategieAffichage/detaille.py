from .StrategieAffichage import StrategieAffichage


class detaille(StrategieAffichage):

    def afficher(self, produits: list) -> list[dict]:
        resultat = []

        for p in produits:
            donnees = {
                "id": p.id,
                "nom": p.nom,
                "prix_total": p.prix_total(),
                "image_url": p.image_url,
                "description": p.description,
                "nb_ventes": p.nb_ventes,
                "est_bundle": p.est_bundle()
            }

            if p.est_bundle():
                donnees["nb_items"] = p.nb_items()

            resultat.append(donnees)

        return resultat
