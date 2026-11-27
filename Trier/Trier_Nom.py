from Trier.StrategieTrier import StrategieTri

class Trier_Nom(StrategieTri):
    def trier(self, composants: list) -> list:
        return sorted(composants, key=lambda composant: composant.nom.lower())