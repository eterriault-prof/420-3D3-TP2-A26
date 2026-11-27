from Trier.StrategieTrier import StrategieTri

class Trier_Popularité(StrategieTri):
    def trier(self, composants: list) -> list:
        return sorted(composants, key=lambda composant: composant.nb_ventes, reverse=True)