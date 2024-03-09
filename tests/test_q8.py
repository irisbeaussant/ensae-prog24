# This will work if ran from the root folder ensae-prog24


import sys
sys.path.append("swap_puzzle/")




import unittest
from graph import Graph
from grid import Grid


class Test_bfsbis(unittest.TestCase):
    def test_bfsbis(self):
        A = Grid.grid_from_file("input/grid5.in")
        B = Grid.grid_from_file("input/grid6.in")
        chemin = A.bfs_bis(A, B)
        self.assertEqual(chemin, [A.state, [[1, 4], [3, 2]], B.state])


if __name__ == '__main__':
   unittest.main()
