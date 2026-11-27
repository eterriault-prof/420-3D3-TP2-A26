from .composant import Composant
from abc import ABC, abstractmethod


class Composite(Composant, ABC):

    def __init__(self, id: int, nom: str, description: str,
                 nb_ventes: int, image_url: str):
        super().__init__(id, nom, description, nb_ventes, image_url)
        self.enfants: list[Composant] = []

    def ajouter(self, enfant: Composant):
        self.enfants.append(enfant)

    def retirer(self, enfant: Composant):
        self.enfants.remove(enfant)

    @abstractmethod
    def prix_total(self) -> float:
        pass

    def nb_items(self) -> int:
        return sum(enfant.nb_items() for enfant in self.enfants)

    def est_bundle(self) -> bool:
        return True
