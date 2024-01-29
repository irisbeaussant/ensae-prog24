# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

class Test_GridLoading(unittest.TestCase):
    def test_graph1(self):
        graph= Grid.grid_from_file("input/graph1.in")
        graph.bfs(self,1,7 )
        self.assertEqual(grid.state, 3)



if __name__ == '__main__':
    unittest.main()