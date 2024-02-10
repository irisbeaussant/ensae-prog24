# This will work if ran from the root folder ensae-prog24


import sys
sys.path.append("swap_puzzle/")




import unittest
from graph import Graph
from grid import Grid


class Test_bfsbis(unittest.TestCase):
    def test_bfsbis(self):
        A = Grid.grid_from_file("input/grid5.in")
        B = [[1, 2], [3, 4]]
        chemin = A.bfs_bis(A.state, B)
        self.assertEqual(chemin, [A.state, [[1, 2], [4, 3]], B])


if __name__ == '__main__':
   unittest.main()
