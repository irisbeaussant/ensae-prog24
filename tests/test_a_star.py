# This will work if ran from the root folder ensae-prog24


import sys
sys.path.append("swap_puzzle/")




import unittest
from graph import Graph
from grid import Grid


class Test_a_star(unittest.TestCase):
    def test_a_star(self):
        A_grid = Grid.grid_from_file("input/grid5.in")
        #A = tuple(tuple(liste) for liste in A_grid.state)
        B_grid = Grid.grid_from_file("input/grid6.in")
        #B = tuple(tuple(liste) for liste in B_grid.state)
        chemin = A_grid.A_star(A_grid, B_grid)
        self.assertEqual(chemin, [A_grid.state, [[1, 2], [4, 3]], B_grid.state])


if __name__ == '__main__':
   unittest.main()
