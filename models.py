"""Modèle Composite pour les produits numériques GameNeuve."""

from abc import ABC, abstractmethod


class Composant(ABC):
    """Contrat commun à tous les éléments du catalogue."""

    def __init__(
        self,
        id: int,
        nom: str,
        description: str,
        prix: float,
        nb_ventes: int,
        image_url: str,
    ) -> None:
        self.id = id
        self.nom = nom
        self.description = description
        self.prix = prix
        self.nb_ventes = nb_ventes
        self.image_url = image_url

    @abstractmethod
    def prix_total(self) -> float:
        """Retourne le prix final de ce composant."""

    @abstractmethod
    def nb_items(self) -> int:
        """Retourne le nombre de produits individuels contenus."""

    @abstractmethod
    def est_bundle(self) -> bool:
        """Indique si le composant est un bundle."""

    def ajouter(self, composant: "Composant") -> None:
        """Les feuilles ne peuvent pas contenir d'autres composants."""
        raise TypeError("Un produit individuel ne peut pas contenir d'enfants.")

    def retirer(self, composant: "Composant") -> None:
        """Les feuilles ne peuvent pas contenir d'autres composants."""
        raise TypeError("Un produit individuel ne peut pas contenir d'enfants.")


class Feuille(Composant):
    """Composant terminal : un produit qui ne contient aucun enfant."""

    def nb_items(self) -> int:
        return 1

    def est_bundle(self) -> bool:
        return False


class Composite(Composant):
    """Composant qui peut contenir des feuilles ou d'autres composites."""

    def __init__(
        self,
        id: int,
        nom: str,
        description: str,
        prix: float,
        nb_ventes: int,
        image_url: str,
    ) -> None:
        super().__init__(id, nom, description, prix, nb_ventes, image_url)
        self.enfants: list[Composant] = []

    def ajouter(self, composant: Composant) -> None:
        if not isinstance(composant, Composant):
            raise TypeError("Un bundle doit contenir un composant du catalogue.")
        if composant is self:
            raise ValueError("Un bundle ne peut pas se contenir lui-même.")
        self.enfants.append(composant)

    def retirer(self, composant: Composant) -> None:
        self.enfants.remove(composant)


class ProduitNumerique(Feuille):
    """Un jeu ou un DLC individuel."""

    def prix_total(self) -> float:
        return round(self.prix, 2)


class Bundle(Composite):
    """Regroupement de produits ou d'autres bundles avec un rabais."""

    def __init__(
        self,
        id: int,
        nom: str,
        description: str,
        prix: float,
        nb_ventes: int,
        image_url: str,
        rabais: float = 0.0,
    ) -> None:
        super().__init__(id, nom, description, prix, nb_ventes, image_url)
        if not 0 <= rabais <= 1:
            raise ValueError("Le rabais doit être compris entre 0 et 1.")
        self.rabais = rabais

    def prix_total(self) -> float:
        # Chaque enfant calcule son propre prix : l'imbrication est récursive.
        sous_total = sum(enfant.prix_total() for enfant in self.enfants)
        return round(sous_total * (1 - self.rabais), 2)

    def nb_items(self) -> int:
        # Une feuille vaut 1; un bundle additionne récursivement ses enfants.
        return sum(enfant.nb_items() for enfant in self.enfants)

    def est_bundle(self) -> bool:
        return True