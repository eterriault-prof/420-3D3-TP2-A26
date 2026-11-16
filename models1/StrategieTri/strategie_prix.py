from .StrategieTrie import StrategieTrie


class strategie_prix(StrategieTrie):
    
    def trier(self, produits) -> list:
        return sorted(produits, key=lambda p: p.prix_total())
        