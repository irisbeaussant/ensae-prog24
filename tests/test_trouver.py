# This will work if ran from the root folder ensae-prog24

import sys
sys.path.append("swap_puzzle/")


import unittest
from grid import Grid

from solver import Solver


class Test_trouver(unittest.TestCase):
    def test_trouver1(self):
        grid = Grid.grid_from_file("input/grid1.in")
        solver = Solver()
        x = solver.trouver(5, grid)
        self.assertEqual(x, (2, 0))

    def test_trouver2(self):
        grid = Grid.grid_from_file("input/grid4.in")
        solver = Solver()
        x = solver.trouver(11, grid)
        self.assertEqual(x, (3, 2))


if __name__ == '__main__':
    unittest.main()
