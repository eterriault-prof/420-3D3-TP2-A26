from .composant import Composant
from abc import ABC

class Feuille(Composant, ABC):
    """Cas de base — un nœud sans enfants."""
    pass