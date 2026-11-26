from strategie.strategie_tri import StrategieTri


class TriParPrix(StrategieTri):
    def trier(self, produits: list) -> list:
        return sorted(produits, key=lambda p: p.prix_total())
