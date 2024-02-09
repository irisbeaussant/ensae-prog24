""" 
This is the graph module. It contains a minimalistic Graph class.
"""
from queue import Queue


from itertools import permutations
import numpy as np

class Graph:
    """
    A class representing undirected graphs as adjacency lists.


    Attributes:
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [neighbor1, neighbor2, ...]
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges.
    edges: list[tuple[NodeType, NodeType]]
        The list of all edges
    """


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


    def add_edge(self, node1, node2):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes.
        When adding an edge between two nodes, if one of the nodes does not exist it is added to the list of nodes.


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


        """
        Question 5 - méthode BFS
        """

    def bfs(self, src, dst):
        """
        Finds a shortest path from src to dst by BFS.


        Parameters:
        ----------
        src: NodeType
            The source node.
        dst: NodeType
            The destination node.


        Output:
        ------
        path: list[NodeType] | None
            The shortest path from src to dst. Returns None if dst is not reachable from src
        """
        file = Queue()
        file.put(src)
        sommets_visites = []
        parents = {}  # est un dictionnaire du type {sommet : voisin parcouru juste avant}
        g = self.graph
        while file:
            x = file.get()
            # x correspond au sommet sur lequel on est actuellement
            if x == dst:  # si on arrive à la destination, il est inutile de parcourir davantage de sommets
                break
            if x not in sommets_visites:
                sommets_visites.append(x)
            for voisin in g[x]:
                if voisin not in sommets_visites:
                    file.put(voisin)
                    parents[voisin] = x
                    sommets_visites.append(voisin)
        chemin = [dst]
        y = dst
        while y != src:
            y = parents[y]
            chemin = [y] + chemin
        return chemin


    """
    Question 7


    nombre de noeuds :
    nombre d'arêtes du graphe :
    complexité de l'algorithme :
    comparaison avec la méthode naïve :


    """
    


    

    #@staticmethod
    #def comp_mat(M, N):   # M et N sont de mêmes dimensions
     #   for i in range(len(M)):
      #      for j in range(len(M[0])):
       #         if M[i, j] != N[i, j]:
        #            return False
       # return True  # signifie que les deux matrices sont identiques

    #@staticmethod
    #def dans_liste(M, N, liste):
     #   for (i, j) in liste:
      #      if Graph.comp_mat(M, i) and Graph.comp_mat(N, j):
       #         return True
       # return False
    # Si le couple de matrices est déjà dans la liste, renvoie true, sinon false

    

    #def liste_noeuds_a_relier(self,m,n ):  # on cherche quels noeuds sont voisins dans le graphe
     #   m=self.m
      #  n=self.n
       # L = []
        #for M1 in g.noeuds(m, n):
         #   for M2 in g.noeuds(m, n):
          #      if not Graph.comp_mat(self, M1, M2):
           #         for i in range(m):
            #            for j in range(n):
             #               if not Graph.dans_liste(Graph, M1, M2, L) and not Graph.dans_liste(Graph, M2, M1, L):
                #                #  if (M1,M2) not in L and (M2,M1) not in L :
               #                 if i+1 < m and (M1[i, j] == M2[i+1, j]):
              #                      L.append((M1, M2))
                 #               if i-1 >= 0 and (M1[i, j] == M2[i-1, j]):
                 #                   L.append((M1, M2))
                  #              if j+1 < n and (M1[i, j] == M2[i, j+1]):
                   #                 L.append((M1, M2))
                    #            if j-1 >= 0 and (M1[i, j] == M2[i, j-1]):
                     #               L.append((M1, M2))
        #return L


   # def graphe_des_grilles(self, g):  # construction du graphe de tous les états de la grille
     #   graphe_grilles = {}
      #  for (i, j) in self.liste_noeuds_a_relier(g.m, g.n, g):
       #    ibis = frozenset(i)
       #    jbis = frozenset(j)
       #    graphe_grilles.add_edge(ibis, jbis)
      # return graphe_grilles

    #def chemin_le_plus_court(self, etatinitial, etatfinal):  # méthod BFS adaptée aux grilles
     #   graphe_grilles = {}
      #  for (i, j) in Grid.liste_noeuds_a_relier():
       #     self.add_edge(i, j)
        #file = Queue()
       # file.put(etatinitial)
        #sommets_visites = []
        #parents = {}  # est un dictionnaire du type {sommet : voisin parcouru juste avant}
        #while file:
         #   x = file.get()
          #  # x correspond au sommet sur lequel on est actuellement
           # if x == etatfinal:  # si on arrive à la destination, il est inutile de parcourir
            #    # davantage de sommets
             #   break
            #if x not in sommets_visites:
             #   sommets_visites.append(x)
            #for voisin in graphe_grilles[x]:
             #   if voisin not in sommets_visites:
              #      file.put(voisin)
               #     parents[voisin] = x
                #    sommets_visites.append(voisin)
        #chemin = [etatfinal]
        #y = etatfinal
        #while y != etatinitial:
          #  y = parents[y]
           # chemin = [y] + chemin
        #return chemin


        # on obtient le chemin le plus court pour arriver à la grille ordonnée, donc les
        #  swap à faire


    """
    Question 8
    Pour ne visiter que la partie du graphe nécessaire pour arriver au noeud de destination,
    il faut le construire au fur et à mesure de son parcours
    """

    #def egal_mat(M, N):
     #   for sublist1, sublist2 in zip(M, N):
      #      if all(element1 == element2 for element1, element2 in zip(sublist1, sublist2)):
       #         return True


    


    @classmethod
    def graph_from_file(cls, file_name):
        """
        Reads a text file and returns the graph as an object of the Graph class.

 
        The file should have the following format:
            The first line of the file is 'n m'
            The next m lines have 'node1 node2'
        The nodes (node1, node2) should be named 1..n


        Parameters:
        -----------
        file_name: str
            The name of the file


        Outputs:
        -----------
        graph: Graph
            An object of the class Graph with the graph from file_name.
        """
        with open(file_name, "r") as file:
            n, m = map(int, file.readline().split())
            graph = Graph(range(1, n+1))
            for _ in range(m):
                edge = list(map(int, file.readline().split()))
                if len(edge) == 2:
                    node1, node2 = edge
                    graph.add_edge(node1, node2)  # will add dist=1 by default
                else:
                    raise Exception("Format incorrect")
        return graph




