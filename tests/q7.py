# This will work if ran from the root folder ensae-prog24


import sys
sys.path.append("swap_puzzle/")


import unittest
from grid import Grid


class Test_Cheminlepluscourt(unittest.TestCase):
    def test_cheminlepluscourt(self):
        A = Grid.grid_from_file("input/grid5.in")
        B = Grid.grid_from_file("input/grid6.in")
        chemin = A.chemin_le_plus_court(A.state, B.state)
        self.assertEqual(chemin, [A.state, [[1, 4], [3, 2]], B.state])

    def test_swaps_a_faire(self):
        A = Grid.grid_from_file("input/grid5.in")
        B = [[1, 2], [3, 4]]
        swaps = A.swaps_a_faire(A.state, B)
        self.assertEqual(swaps, [((0, 1), (1, 1)), ((1, 1), (0, 1))])

if __name__ == '__main__':
   unittest.main()
