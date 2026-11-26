from typing import override

from composant import Composant
from abc import ABC

class Composite(Composant, ABC):
    """Nœud intermédiaire — délègue à ses enfants."""

    def __init__(self, id: int, nom: str, description: str,
                 nb_ventes: int, image_url: str, rabais: float = 0.0):
        super().__init__(id, nom, description, nb_ventes, image_url)
        self.items: list[Composant] = []
        self.rabais = rabais

    def ajouter_items(self, item: Composant) -> None:
        self.items.append(item)

    def retirer_items(self, item: Composant) -> None:
        self.items.remove(item)

    @override
    def prix_total(self) -> float:
        return sum(p.prix_total() for p in self.items) * (1 - self.rabais)

    @override
    def nb_items(self) -> int:
        return sum(p.nb_items() for p in self.items)

    @override
    def est_bundle(self) -> bool:
        return True

class Bundle(Composite):
    pass
        