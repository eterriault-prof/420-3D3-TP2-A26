from abc import ABC, abstractmethod

class StrategieTri(ABC):
    @abstractmethod
    def trier(self, produits: list) -> list:
        pass