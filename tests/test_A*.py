import sys
sys.path.append("swap_puzzle/")



import unittest
from grid import Grid
Grid



class Test_A(unittest.TestCase):
    def test_A(self):
        M = Grid.grid_from_file("input/grid5.in")
        chemin = M.A(M.state)
        self.assertEqual(chemin,[M.state, [[1, 4], [3, 2]], gOrd])

if __name__ == '__main__':
   unittest.main()
