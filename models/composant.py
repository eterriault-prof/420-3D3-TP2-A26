from abc import ABC, abstractmethod

class Composant(ABC):

    def __init__(self, id: int, nom: str, description: str, prix: float,
                 nb_ventes: int, image_url: str):
        self.id = id
        self.nom = nom
        self.description = description
        self.prix = prix
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