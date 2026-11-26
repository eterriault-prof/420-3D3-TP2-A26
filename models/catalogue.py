import json
import re
import sys
from pathlib import Path

from .composant import Composant

# Les modules du patron Composite utilisent encore des imports absolus.
# Cet alias permet de les importer comme membres du paquet ``models`` sans
# modifier les fichiers du patron Composite.
sys.modules.setdefault("composant", sys.modules[Composant.__module__])

from .composite import Bundle
from .feuille import ProduitNumerique
from strategie.affichage_compact import AffichageCompact
from strategie.affichage_detaille import AffichageDetaille
from strategie.strategie_affichage import StrategieAffichage
from strategie.strategie_tri import StrategieTri
from strategie.tri_par_nom import TriParNom
from strategie.tri_par_popularite import TriParPopularite
from strategie.tri_par_prix import TriParPrix


class Catalogue:

    def __init__(
        self,
        chemin_json: str,
        strategie_tri: StrategieTri | None = None,
        strategie_affichage: StrategieAffichage | None = None,
    ):
        self._produits: dict[int, Composant] = {}
        self._strategie_tri = strategie_tri or TriParNom()
        self._strategie_affichage = strategie_affichage or AffichageCompact()
        self._charger(chemin_json)

    def _charger(self, chemin: str) -> None:
        contenu = Path(chemin).read_text(encoding="utf-8")

        # Le fichier fourni contient des commentaires /* ... */, qui ne font
        # pas partie de la norme JSON. On les ignore sans modifier les donnees.
        contenu = re.sub(r"/\*.*?\*/", "", contenu, flags=re.DOTALL)
        donnees = json.loads(contenu)

        for d in donnees:
            if d["type"] == "produit":
                produit = ProduitNumerique(
                    id=d["id"],
                    nom=d["nom"],
                    description=d["description"],
                    prix=d["prix"],
                    nb_ventes=d["nb_ventes"],
                    image_url=d["image_url"],
                )
            else:
                produit = Bundle(
                    id=d["id"],
                    nom=d["nom"],
                    description=d["description"],
                    nb_ventes=d["nb_ventes"],
                    image_url=d["image_url"],
                    rabais=d.get("rabais", 0.0),
                )
            self._produits[produit.id] = produit

        for d in donnees:
            if d["type"] == "bundle":
                bundle = self._produits[d["id"]]
                for enfant_id in d.get("enfants", []):
                    bundle.ajouter_items(self._produits[enfant_id])

    def tous(self) -> list[Composant]:
        return list(self._produits.values())

    def obtenir(self, id: int) -> Composant | None:
        return self._produits.get(id)

    def definir_strategie_tri(self, strategie: StrategieTri) -> None:
        self._strategie_tri = strategie

    def definir_strategie_affichage(
        self, strategie: StrategieAffichage
    ) -> None:
        self._strategie_affichage = strategie

    def afficher_produits(
        self,
        strategie_tri: StrategieTri | str | None = None,
        strategie_affichage: StrategieAffichage | str | None = None,
    ) -> list[dict]:
        """Trie puis formate les produits en deleguant aux deux strategies.

        Les chaines sont acceptees temporairement pour conserver la
        compatibilite avec le frontend fourni, que ce projet ne doit pas
        modifier en dehors de sa section balisee.
        """
        tri = self._resoudre_tri(strategie_tri)
        affichage = self._resoudre_affichage(strategie_affichage)
        return affichage.afficher(tri.trier(self.tous()))

    def _resoudre_tri(
        self, strategie: StrategieTri | str | None
    ) -> StrategieTri:
        if strategie is None:
            return self._strategie_tri
        if isinstance(strategie, StrategieTri):
            return strategie

        strategies = {
            "nom": TriParNom,
            "prix": TriParPrix,
            "popularite": TriParPopularite,
        }
        try:
            return strategies[strategie]()
        except (KeyError, TypeError) as exc:
            raise ValueError(f"Strategie de tri inconnue : {strategie}") from exc

    def _resoudre_affichage(
        self, strategie: StrategieAffichage | str | None
    ) -> StrategieAffichage:
        if strategie is None:
            return self._strategie_affichage
        if isinstance(strategie, StrategieAffichage):
            return strategie

        strategies = {
            "compact": AffichageCompact,
            "detaille": AffichageDetaille,
        }
        try:
            return strategies[strategie]()
        except (KeyError, TypeError) as exc:
            raise ValueError(
                f"Strategie d'affichage inconnue : {strategie}"
            ) from exc
