class ProduitNumerique:
    """Un jeu ou un DLC individuel."""

    def __init__(self, id: int, nom: str, description: str, prix: float,
                 nb_ventes: int, image_url: str):
        self.id = id
        self.nom = nom
        self.description = description
        self.prix = prix
        self.nb_ventes = nb_ventes
        self.image_url = image_url

    def prix_total(self) -> float:
        return self.prix

    def nb_items(self) -> int:
        return 1

    def est_bundle(self) -> bool:
        return False


class Bundle:
    """Un regroupement de produits numériques ou d'autres bundles."""

    def __init__(self, id: int, nom: str, description: str, prix: float,
                 nb_ventes: int, image_url: str, rabais: float = 0.0):
        self.id = id
        self.nom = nom
        self.description = description
        self.prix = prix
        self.nb_ventes = nb_ventes
        self.image_url = image_url
        self.rabais = rabais
        self.enfants = []

    def ajouter(self, enfant) -> None:
        self.enfants.append(enfant)

    def prix_total(self) -> float:
        total = 0.0
        for enfant in self.enfants:
            if isinstance(enfant, ProduitNumerique):
                total += enfant.prix
            elif isinstance(enfant, Bundle):
                sous_total = 0.0
                for sous_enfant in enfant.enfants:
                    if isinstance(sous_enfant, ProduitNumerique):
                        sous_total += sous_enfant.prix
                    elif isinstance(sous_enfant, Bundle):
                        for sous_sous_enfant in sous_enfant.enfants:
                            if isinstance(sous_sous_enfant, ProduitNumerique):
                                sous_total += sous_sous_enfant.prix
                total += sous_total * (1 - enfant.rabais)
        return round(total * (1 - self.rabais), 2)

    def nb_items(self) -> int:
        total = 0
        for enfant in self.enfants:
            if isinstance(enfant, ProduitNumerique):
                total += 1
            elif isinstance(enfant, Bundle):
                for sous_enfant in enfant.enfants:
                    if isinstance(sous_enfant, ProduitNumerique):
                        total += 1
                    elif isinstance(sous_enfant, Bundle):
                        for sous_sous_enfant in sous_enfant.enfants:
                            if isinstance(sous_sous_enfant, ProduitNumerique):
                                total += 1
        return total

    def est_bundle(self) -> bool:
        return True
