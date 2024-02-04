# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from graph import Graph


class Test_bfs(unittest.TestCase):
    def test_graph1(self):
        graph = Graph.graph_from_file("input/graph1.in")
        graph.bfs(self,1,3)
        self.assertEqual([1,15,3])

if __name__ == '__main__':
    unittest.main()