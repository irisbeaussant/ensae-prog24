# This will work if ran from the root folder ensae-prog24


import sys
sys.path.append("swap_puzzle/")




import unittest
from graph import Graph
from grid import Grid


class Test_a_star(unittest.TestCase):
    def test_a_star1(self):
        A_grid = Grid.grid_from_file("input/grid5.in")
        B_grid = Grid.grid_from_file("input/grid6.in")
        chemin = A_grid.A_star(A_grid, A_grid, B_grid)
        self.assertEqual(chemin, [A_grid.state, [[1, 4], [3, 2]], B_grid.state])
    
    def test_a_star2(self):
        A_grid = Grid.grid_from_file("input/grid7.in")
        B_grid = Grid.grid_from_file("input/grid8.in")
        chemin = A_grid.A_star(A_grid, A_grid, B_grid)
        self.assertEqual(chemin, [A_grid.state, [[1, 2, 6], [4, 5, 3], [7, 8, 9]], B_grid.state])

    def test_a_star3(self):
        A_grid = Grid.grid_from_file("input/grid9.in")
        B_grid = Grid.grid_from_file("input/grid10.in")
        chemin = A_grid.A_star(A_grid, A_grid, B_grid)
        self.assertEqual(chemin, [A_grid.state, [[1, 2, 3, 4], [5, 7, 6, 8], [9, 10, 11, 12]], B_grid.state])


if __name__ == '__main__':
   unittest.main()
