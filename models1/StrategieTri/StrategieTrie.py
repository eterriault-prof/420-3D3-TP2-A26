from abc import ABC, abstractmethod

class StrategieTrie(ABC):

    @abstractmethod
    def trier(self, produits) -> list:
        pass

