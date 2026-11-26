from strategie.strategie_tri import StrategieTri


class TriParNom(StrategieTri):
    """Stratégie de tri par nom."""
    def trier(self, produits: list) -> list:
        return sorted(produits, key=lambda p: p.nom.lower())
