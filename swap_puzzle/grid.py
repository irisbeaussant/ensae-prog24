"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random

class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The initial state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorted and returns the answer as a boolean.
        """
        for i in range (self.m):
            for j in range (self.n-1):
                if self.state[i][j]>self.state[i][j+1]:
                    return False
        return True

        """
        testé : ok
        """

        

    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        if abs(cell1[0]-cell2[0])!=1 and abs(cell1[1]-cell2[1])!=1:
            return "pas le droit d'échanger"
        else:
            (self.state[cell1[0]][cell1[1]],self.state[cell2[0]][cell2[1]])=(self.state[cell2[0]][cell2[1]],self.state[cell1[0]][cell1[1]])
        
        """
        testé : ok
        """
       

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for i in range(len(cell_pair_list)):
            Grid.swap(self,cell_pair_list[i][0],cell_pair_list[i][1])
        """
        testé : ok
        """    


    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output:
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid


import numpy as np
import matplotlib.pyplot as plt



    def representation_graphique(grid):
     arr = np.array(grid)
     fig, ax = plt.subplots()
     img = ax.imshow(arr, cmap='viridis')
     plt.show()

    
        """
        Question 6 :
        Les noeuds sont de type hashable donc il faut transformer chaque grille en un élément non mutable, par exemple un frozenset.
        """
from itertools import permutations
import numpy as np

    def noeuds(m,n):
        l=[k for k in range (1,(m*n+1))] #on crée la liste de tous les nombres contenus dans la grille
        perm=list(permutations(l,m*n))
        toutes_grilles=[]
        for i in perm:
         i=np.array(i).reshape((m,n))
            toutes_grilles.append(i)
        return toutes_grilles


    def hash(grid): #rend hashable
        gridbis=frozenset(grid)
        return gridbis



        """
        Question 7
        """

        class graph:

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 

        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes 
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.edges = []
        
    def __str__(self):
        """
        Prints the graph as a list of neighbors for each node (one per line)
        """
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the graph with number of nodes and edges.
        """
        return f"<graph.Graph: nb_nodes={self.nb_nodes}, nb_edges={self.nb_edges}>"




from itertools import permutations
import numpy as np

m=2
n=2


def hash(grid):
    gridbis=frozenset(grid)
    return gridbis


def noeuds(m,n):
    l=[k for k in range (1,(m*n+1))] #on crée la liste de tous les nombres contenus dans la grille
    perm=list(permutations(l,m*n))
    toutes_grilles=[]
    for i in perm:
        i=np.array(i).reshape((m,n))
        toutes_grilles.append(i)
#        toutes_grilles.append(hash(i))
    return toutes_grilles


def liste_noeuds_a_relier ():
    L=[]     #ça sera une liste de couples, les couples sont deux grilles entre lesquelles on veut un edge
    for a in range (0,m*n): #tu prends une grille dans ta liste noeuds
        for b in range (0,m*n): #tu prends une autre grille, et on va comparer les deux
            if b!=a:
                print("1")
                for i in range (1,m-1):
                    print("2")#je mets ces bornes pour pas être out of range, je verrai le reste plus loin
                    for j in range (1,n-1):
                        print("bonjour")#on prend un élément de la première matrice et on regarde s'il a été décalé d'un cran dans la deuxième matrice
                        if noeuds(m,n)[a][i,j]==noeuds(m,n)[b][1-i,j] or noeuds(m,n)[a][i,j]==noeuds(m,n)[b][i+1,j] or noeuds(m,n)[a][i,j]==noeuds(m,n)[b][i,j+1] or noeuds(m,n)[a][i,j]==noeuds(m,n)[b][i,j-1]:
                            L.append ((noeuds(m,n)[a],noeuds(m,n)[b]))
                            
               
                    #ici commencent les cas particuliers

                    #cas 1: on se déplace sur la ligne d'indice 0 de noeud[a]
                if noeuds(m,n)[a][0,0]==noeuds(m,n)[b][0,1] or noeuds(m,n)[a][0,0]==noeuds(m,n)[b][1,0]:
                    L.append((noeuds[a]),noeuds[b])
                if noeuds(m,n)[a][0,n-1]==noeuds(m,n)[b][0,n-2] or noeuds(m,n)[a][0,n-1]==noeuds(m,n)[b][1,n-1]:
                    L.append((noeuds(m,n)[a],noeuds(m,n)[b]))
                for j in range (1,n-1):
                    if noeuds(m,n)[a][0,j]==noeuds(m,n)[b][0,j-1] or noeuds(m,n)[a][0,j]==noeuds(m,n)[b][0,j+1] or noeuds(m,n)[a][0,j]==noeuds(m,n)[b][1,j]:
                        L.append((noeuds(m,n)[a],noeuds(m,n)[b]))

                     #cas 2: on se déplace sur la ligne d'indice m-1 de noeud[a]
                if noeuds(m,n)[a][m-1,0]==noeuds(m,n)[b][m-1,1] or noeuds(m,n)[a][m-1,0]==noeuds(m,n)[b][m-2,0]:
                    L.append((noeuds(m,n)[a],noeuds(m,n)[b]))
                if noeuds(m,n)[a][m-1,n-1]==noeuds(m,n)[b][m-2,n-1] or noeuds(m,n)[a][m-1,n-1]==noeuds(m,n)[b][m-1,n-2]:
                    L.append((noeuds(m,n)[a],noeuds(m,n)[b]))
                for j in range (1,n-2):
                    if noeuds(m,n)[a][m-1,j]==noeuds(m,n)[b][m-1,j-1] or noeuds(m,n)[a][m-1,j]==noeuds(m,n)[b][m-1,j+1] or noeuds(m,n)[a][m-1,j]==noeuds(m,n)[b][m-2,j]:
                        L.append((noeuds(m,n)[a],noeuds(m,n)[b]))

                    #cas 3: on se déplace sur la colonne d'indice 0 de noeud[a]
                for i in range (1, m-1):
                    if noeuds(m,n)[a][i,0]==noeuds(m,n)[b][i+1,0] or noeuds(m,n)[a][i,0]==noeuds(m,n)[b][i-1,0] or noeuds(m,n)[a][i,0]==noeuds(m,n)[b][i,1]:
                        L.append((noeuds(m,n)[a],noeuds(m,n)[b]))

                    #cas 4: on se déplace sur la colonne d'indice n-1 de noeud[a]
                for i in range (1, m-1):
                    if noeuds(m,n)[a][i,n-1]==noeuds(m,n)[b][i+1,n-1] or noeuds(m,n)[a][i,n-1]==noeuds(m,n)[b][i-1,n-1] or noeuds[a][i,n-1]==noeuds[b][i,n-2]:
                        L.append((noeuds(m,n)[a],noeuds(m,n)[b]))
                        
    return L

def add_edge(self, node1, node2):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 
        When adding an edge between two nodes, if one of the ones does not exist it is added to the list of nodes.

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
            self.nb_edges += 1
            self.edges.append((node1, node2))

graph_bis=graph(noeuds)
def final():
    for (i,j) in liste_noeuds_a_relier:
        graph_bis.add_edge(i,j)
