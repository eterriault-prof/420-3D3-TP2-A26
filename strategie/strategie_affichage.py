from abc import ABC, abstractmethod


class StrategieAffichage(ABC):
    @abstractmethod
    def afficher(self, produits: list) -> list[dict]:
        pass
