from .StrategieTrie import StrategieTrie


class strategie_nom(StrategieTrie):
    
    def trier(self, produits) -> list:
        return sorted(produits, key=lambda p: p.nom.lower())
        