from typing import override

from composant import Composant
from abc import ABC

class Feuille(Composant, ABC):
    """Cas de base — un nœud sans enfants."""
    pass

class ProduitNumerique(Feuille):
    """Un jeu ou un DLC individuel."""

    def __init__(self, id: int, nom: str, description: str, prix: float,
                 nb_ventes: int, image_url: str):
        super().__init__(id, nom, description, nb_ventes, image_url)
        self.prix = prix

    @override
    def prix_total(self) -> float:
        return self.prix
    @override
    def nb_items(self) -> int:
        return 1
    @override
    def est_bundle(self) -> bool:
        return False