from abc import ABC, abstractmethod


class StrategieAffichage(ABC):
    @abstractmethod
    def afficher(self, composants: list) -> list[dict]:
        pass