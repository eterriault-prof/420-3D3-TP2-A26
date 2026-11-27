from Affichage.StrategieAffichage import StrategieAffichage

class Afficher_Compact(StrategieAffichage):

    def afficher(self, composants: list) -> list[dict]:
        resultat = []

        for p in composants:
            resultat.append({
                "id": p.id,
                "nom": p.nom,
                "prix_total": p.prix_total(),
                "image_url": p.image_url,
                "est_bundle": p.est_bundle(),
            })

        return resultat