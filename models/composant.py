from abc import ABC, abstractmethod


class Composant(ABC):

    def __init__(self, id: int, nom: str, description: str,
                 nb_ventes: int, image_url: str):
        self.nom: str = nom
        self.id = id
        self.description = description
        self.nb_ventes = nb_ventes
        self.image_url = image_url

    @abstractmethod
    def prix_total(self) -> float:
        pass

    @abstractmethod
    def nb_items(self) -> int:
        pass

    @abstractmethod
    def est_bundle(self) -> bool:
        pass