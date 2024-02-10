# This will work if ran from the root folder ensae-prog24
import sys
sys.path.append("swap_puzzle/")


import unittest

from graph import Graph


class Test_bfs(unittest.TestCase):
    def test_graph1(self):
        g = Graph.graph_from_file("input/graph1.in")
        self.assertIn(g.bfs(1, 3), [[1, 15, 3], [1, 18, 3]])   # Le fichier graph1.path.out montre
        # que le chemin le plyus court entre 1 et 3 passe par 15 mais si on regarde les différentes
        # arêtes on voit qu'il y a un chemin de même longueur passant par 18, il y a donc deux
        # possibilités de chemin le plus court allant de 1 à 3

    def test_graph2(self):
        g = Graph.graph_from_file("input/graph2.in")
        self.assertEqual(g.bfs(2, 7), [2, 17, 7])


if __name__ == '__main__':
   unittest.main()
