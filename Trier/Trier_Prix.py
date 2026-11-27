from Trier.StrategieTrier import StrategieTri

class Trier_Prix(StrategieTri):

    def trier(self, composants: list) -> list:
        return sorted(
            composants,
            key=lambda composant: composant.prix_total()
        )