from .StrategieTrie import StrategieTrie


class strategie_populaire(StrategieTrie):
    
    def trier(self, produits) -> list:
        return sorted(produits, key=lambda p: p.nb_ventes, reverse=True)
        