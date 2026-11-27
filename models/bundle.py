from .composite import Composite


class Bundle(Composite):

    def __init__(self, id: int, nom: str, description: str,
                 nb_ventes: int, image_url: str, rabais: float):

        super().__init__(id, nom, description, nb_ventes, image_url)
        self.rabais = rabais

    def prix_total(self) -> float:
        prix = sum(enfant.prix_total() for enfant in self.enfants)
        return round(prix * (1 - self.rabais), 2)