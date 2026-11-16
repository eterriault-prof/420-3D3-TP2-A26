from .StrategieAffichage import StrategieAffichage


class compact(StrategieAffichage):

    def afficher(self, produits: list) -> list[dict]:
        resultat = []

        for p in produits:
            donnees = {
                "id": p.id,
                "nom": p.nom,
                "prix_total": p.prix_total(),
                "image_url": p.image_url,
                "est_bundle": p.est_bundle()
            }

            resultat.append(donnees)

        return resultat
