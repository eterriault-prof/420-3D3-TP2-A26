from abc import ABC, abstractmethod


class StrategieTri(ABC):
    @abstractmethod
    def trier(self, composants: list) -> list:
        pass