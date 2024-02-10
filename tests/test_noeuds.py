# This will work if ran from the root folder ensae-prog24


import sys
sys.path.append("swap_puzzle/")

import unittest
from grid import Grid
import graph


class Test_noeuds(unittest.TestCase):
    def test_noeuds1(self):
        A = Grid.grid_from_file("input/grid5.in")
        liste = A.noeuds()
        self.assertEqual(len(liste), 24)  # on vérifie qu'il y a bien le bon nombre de matrices

    def test_noeuds2(self):  # ce test permet de vérifier que chaque grille est différente
        A = Grid.grid_from_file("input/grid5.in")
        liste = A.noeuds()
        liste_bis = []
        compteur = 0
        for k in liste:
            for j in liste_bis:
                if graph.comp_mat(k, j):
                    liste_bis.append(k)
                else:
                    compteur += 1
        self.assertEqual(compteur, 0)

        # les deux tests permettent de vérifier que la liste renvoyée par la fonction noeuds
        # renvoie le bon nombre de grilles et qu'elles sont toutes différents
        # On vérifie ainsi que la fonction noeuds renvoie bien toutes les grilles possibles.
  
        
if __name__ == '__main__':
   unittest.main()
