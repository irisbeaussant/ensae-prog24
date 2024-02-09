# This will work if ran from the root folder ensae-prog24


import sys
sys.path.append("swap_puzzle/")


import unittest
from grid import Grid


class Test_Cheminlepluscourt(unittest.TestCase):
    def test_cheminlepluscourt(self):
        A = Grid.grid_from_file("input/grid5.in")
        B = [[1, 2], [3, 4]]
        chemin = A.chemin_le_plus_court(A, B)
        self.assertEqual(chemin, [A, [[1, 2], [4, 3]], B])






if __name__ == '__main__':
   unittest.main()
