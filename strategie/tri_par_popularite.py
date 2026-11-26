from strategie.strategie_tri import StrategieTri


class TriParPopularite(StrategieTri):

    def trier(self, produits: list) -> list:
        return sorted(produits, key=lambda p: p.nb_ventes, reverse=True)
