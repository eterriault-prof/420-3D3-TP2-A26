import unittest

from models import ProduitNumerique, Bundle
from Trier.Trier_Nom import Trier_Nom
from Trier.Trier_Prix import Trier_Prix
from Trier.Trier_Popularité import Trier_Popularité
from Affichage.Afficher_Compact import Afficher_Compact
from Affichage.Afficher_Détaillé import Afficher_Détaillé


class TestStrategies(unittest.TestCase):

    def setUp(self):
        self.jeu = ProduitNumerique(
            1, "Zelda", "Jeu aventure", 100, 10, "/jeu.jpg"
        )
        self.dlc = ProduitNumerique(
            2, "animal Crossing", "Extension", 50, 30, "/dlc.jpg"
        )
        self.bundle = Bundle(
            3, "Bundle", "Collection", 0, 20, "/bundle.jpg", rabais=0.20
        )
        self.bundle.ajouter(self.jeu)
        self.bundle.ajouter(self.dlc)
        self.composants = [self.jeu, self.dlc, self.bundle]

    def test_tri_nom(self):
        resultat = Trier_Nom().trier(self.composants)
        self.assertEqual(resultat, [self.dlc, self.bundle, self.jeu])

    def test_tri_prix(self):
        resultat = Trier_Prix().trier(self.composants)
        self.assertEqual(resultat, [self.dlc, self.jeu, self.bundle])

    def test_tri_popularite(self):
        resultat = Trier_Popularité().trier(self.composants)
        self.assertEqual(resultat, [self.dlc, self.bundle, self.jeu])

    def test_affichage_compact(self):
        resultat = Afficher_Compact().afficher([self.jeu])
        self.assertEqual(resultat, [{
            "id": 1,
            "nom": "Zelda",
            "prix_total": 100,
            "image_url": "/jeu.jpg",
            "est_bundle": False,
        }])

    def test_affichage_detaille(self):
        resultat = Afficher_Détaillé().afficher([self.jeu])
        self.assertEqual(resultat, [{
            "id": 1,
            "nom": "Zelda",
            "prix_total": 100,
            "image_url": "/jeu.jpg",
            "est_bundle": False,
            "description": "Jeu aventure",
            "nb_ventes": 10,
        }])

    def test_affichage_bundle(self):
        resultat = Afficher_Détaillé().afficher([self.bundle])
        self.assertEqual(len(resultat), 1)
        self.assertTrue(resultat[0]["est_bundle"])
        self.assertEqual(resultat[0]["nb_items"], 2)
        self.assertEqual(resultat[0]["prix_total"], 120)
        compact = Afficher_Compact().afficher([self.bundle])
        self.assertTrue(compact[0]["est_bundle"])
        self.assertEqual(compact[0]["prix_total"], 120)
        self.assertNotIn("nb_items", compact[0])

    def test_liste_vide(self):
        for strategie in [Trier_Nom(), Trier_Prix(), Trier_Popularité()]:
            self.assertEqual(strategie.trier([]), [])
        for strategie in [Afficher_Compact(), Afficher_Détaillé()]:
            self.assertEqual(strategie.afficher([]), [])

    def test_tri_sans_modification(self):
        original = self.composants.copy()
        for strategie in [Trier_Nom(), Trier_Prix(), Trier_Popularité()]:
            strategie.trier(self.composants)
            self.assertEqual(self.composants, original)


if __name__ == "__main__":
    unittest.main()
