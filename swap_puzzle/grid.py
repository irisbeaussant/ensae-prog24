from itertools import permutations
import numpy as np
import random
from itertools import permutations
import matplotlib as plt
from graph import Graph
from queue import Queue
import heapq

"""
This is the grid module. It contains the Grid class and its associated methods.
"""


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
  
    def __init__(self, m, n, initial_state=[]):
        """
        Initializes the grid.


        Parameters:
        ----------
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
        for i in range(self.m):
            for j in range(self.n-1):
                if self.state[i][j] > self.state[i][j+1]:
                    return False
        return True

        """
        testé : ok
        """

    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is
        not allowed.


        Parameters:
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the
            column number of the cell.
        """
        if abs(cell1[0]-cell2[0]) != 1 and abs(cell1[1]-cell2[1]) != 1:
            print("cannot be swaped")
        else:
            (self.state[cell1[0]][cell1[1]], self.state[cell2[0]][cell2[1]]) = (self.state[cell2[0]][cell2[1]], self.state[cell1[0]][cell1[1]])
       
        """
        testé : ok
        """
     
    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps.


        Parameters:
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of
            integers).
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for i in range(len(cell_pair_list)):
            self.swap(cell_pair_list[i][0], cell_pair_list[i][1])

        """
        testé : ok
        """

    @classmethod
    def grid_from_file(cls, file_name):
        """
        Creates a grid object from class Grid, initialized with the information from the file
        file_name.
      
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

    """

    Question 4
    Représentation graphique de la grille

    """

    def representation_graphique(self):
        grille = np.array([[0 for i in range(self.n)] for j in range(self.m)])
        plt.imshow(grille)
        for i in range(self.state.shape[0]):
            for j in range(self.state.shape[1]):
                plt.text(j, i, str(self.state[i][j]))
        plt.colorbar()
        plt.show()

    def representation_graphique_bis(self):  # représentation sous la forme d'un tableau
        grille = self.state
        fig, ax = plt.subplots()
        ax.set_axis_off()
        ax.table(cellText=grille, cellLock='center')
        plt.show()

    """
    Question 6 :
    Les noeuds sont de type hashable donc il faut transformer chaque grille en un élément non
    mutable, on les transforme en tuples

    Afin de créer toutes les grilles possibles on trouve toutes les permutations

    """

    def noeuds(self):
        m = self.m
        n = self.n
        liste = [k for k in range(1, (m*n+1))]  # on crée la liste de tous les nombres contenus
        # dans la grille
        perm = tuple(permutations(liste))  # hashable
        toutes_grilles = []
        for i in perm:
            i = np.array(i).reshape((m, n))
            i = tuple(tuple(element) for element in i)
            toutes_grilles.append(i)
        return toutes_grilles  # renvoie une liste contenant toutes les grilles possibles

    """

    Question 7

    -Pour créer tous les noeuds on permute une liste de longueur m*n donc il y a (mn)! noeuds

    -A partir d'une grille mxn on peut réaliser m(n-1) swaps entre deux cases adjacentes 
     horizontalement et n(m-1) swaps entre deux cases adjacentes verticalement.
     Une grille a donc m(n-1)+n(m-1) voisins.
     Or si un noeud N1 est relié à N2 on a forcément N2 relié à N1, et ce par une unique arête.
     Ainsi il y a (m*n)!*(m(n-1)+n(m-1))/2 arêtes

    -ordre de grandeur de la complexité de la méthode bfs:
        -dans le meilleur des csa la grille est triée et la complkexité est en temps constant
        -dans le pire des cas on parcourt tous les sommets du graphe, alors la complexité
        est en O((m*n)!)
        -en moyenne on peut supposer qu'il n'y a pas de raison qu'une grille prise au hasard soit
        plus ou moin loin de la destination, donce en moyenne la complexité est en O((m*n)!/2)
        donc en O(m*n)!
        -cela correspond à une complexité bien plus importante que celle de la méthode naïve
       

        -cependant la methode bfs appliquée aux grilles utilise également la fonction
        liste_noeuds_a_relier qui a une complexité en O((mn)!³*(mn)²), ce qui est implique
        que la méthode bfs appliquée aux grilles a une complexité d'autant plus importante
        que la méthode naïve à cause de la factorielle

    """

    @staticmethod
    # permet de vérifier si deux listes de listes sont égales
    def comp_mat(M, N):   # M et N sont de mêmes dimensions
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] != N[i][j]:
                    return False
        return True  # signifie que les deux matrices sont identiques

    @staticmethod
    # permet de vérifier si un couple de liste de listes est présent dans une liste de couples 
    # de listes de listes
    def dans_liste(M, N, liste):
        for (i, j) in liste:
            if Grid.comp_mat(M, i) and Grid.comp_mat(N, j):
                return True
        return False
    # Si le couple de matrices est déjà dans la liste, renvoie true, sinon false

    def liste_noeuds_a_relier(self):  # on cherche quels noeuds sont voisins dans le graphe
        m = self.m
        n = self.n
        L = []
        for M1 in self.noeuds():
            M11 = [list(t) for t in M1]
            for M2 in self.noeuds():
                M21 = [list(t) for t in M2]
                if not Grid.comp_mat(M11, M21):
                    for i in range(m):
                        for j in range(n):
                            if not Grid.dans_liste(M11, M21, L) and not Grid.dans_liste(M21, M11, L):
                                #  if (M1,M2) not in L and (M2,M1) not in L :
                                if i+1 < m and (M1[i][j] == M2[i+1][j]) and (M1[i+1][j] == M2[i][j]):
                                    L.append((M1, M2))
                                if i-1 >= 0 and (M1[i][j] == M2[i-1][j]) and (M1[i-1][j] == M2[i][j]):
                                    L.append((M1, M2))
                                if j+1 < n and (M1[i][j] == M2[i][j+1]) and (M1[i][j+1] == M2[i][j]):
                                    L.append((M1, M2))
                                if j-1 >= 0 and (M1[i][j] == M2[i][j-1]) and (M1[i][j-1] == M2[i][j]):
                                    L.append((M1, M2))
        return L
        # renvoie une liste de couples qui sont voisins

    # méthode BFS adaptée aux grilles
    # chemin_le_plus_court renvoie le chemin le plus court entre la source et la destination
    def chemin_le_plus_court(self, etatinitial, etatfinal):
        graphe_grilles = Graph(Grid.noeuds(self))
        for (i, j) in self.liste_noeuds_a_relier():
            graphe_grilles.add_edge(i, j)

        src = tuple(tuple(element) for element in etatinitial)
        dst = tuple(tuple(element) for element in etatfinal)
        solution = graphe_grilles.bfs(src, dst)
        sol = [[list(t) for t in G] for G in solution]
        return sol
        solution = graphe_grilles.bfs(etatinitial, etatfinal)
        return solution

    # swaps_a_faire complète le résultat de chemin_le_plus_court en renvoyant les swaps nécessaires
    # pour réaliser ce chemin

    def swaps_a_faire(self, etatinitial, etatfinal):
        liste_grilles = Grid.chemin_le_plus_court(self, etatinitial, etatfinal)
        m = len(etatinitial)
        n = len(etatinitial[1])
        for i in range(len(liste_grilles)-1):  # il faut mettre -1 car le dernier élément
            # ne peut pas être comparé avec l'élément suivant, qui n'existe pas
            swaps = []
            M = liste_grilles[i]
            for j in range(m):
                for k in range(n):
                    if (k+1) < n and M[j][k] == liste_grilles[i+1][j][k+1]:
                        swaps.append(((j, k), (j, k+1)))
                    if (k-1) >= 0 and M[j][k] == liste_grilles[i+1][j][k-1]:
                        swaps.append(((j, k), (j, k-1)))
                    if (j+1) < m and M[j][k] == liste_grilles[i+1][j+1][k]:
                        swaps.append(((j, k), (j+1, k)))
                    if (j-1) >= 0 and M[j][k] == liste_grilles[i+1][j-1][k]:
                        swaps.append(((j, k), (j-1, k)))
        return swaps

    """
    Question 8

    Pour ne visiter que la partie du graphe nécessaire pour arriver au noeud de destination,
    il faut le construire au fur et à mesure de son parcours
    
    """

    def bfs_bis(self, src, dst):
        file = Queue()
        sommets_visites = []
        parents = {}  # est un dictionnaire du type {sommet : voisin parcouru juste avant}
        g = {}  # on initialise le dictionnaire du graphe
        while file:
            x = file.get()
            if x == dst:
                break
            if x not in sommets_visites:
                if x not in g:
                    g[x] = []    # on crée le dictionnaire au fur et à mesure qu'on en a besoin
                    for (i, j) in Grid.liste_noeuds_a_relier(self):
                        i1 = [list(t) for t in i]
                        j1 = [list(t) for t in j]
                        if Grid.comp_mat(self, x, i1):
                            g[x].append(j)
                        elif Graph.comp_mat(self, j1, x):
                            g[x].append(i)
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
    Algorithme A*
    """

    @staticmethod
    def calcul_coordonnees(x, m, n):
        i = (x-1) // n
        j = (x-1) % n
        return (i, j)

    @staticmethod
    def dist_cases(c1, c2):
        x1, y1 = c1
        x2, y2 = c2
        d = abs(x1-x2)+abs(y1-y2)
        return d
        # renvoie la distance entre deux cases au sein d'une grille

    @staticmethod
    def borne_inf_a_dst(G):
        inf = 0
        G = list(list(element) for element in G)
        for i in range(len(G)):
            for j in range(len(G[0])):
                x = G[i][j]
                if Grid.calcul_coordonnees(x, len(G), len(G[0])) != (i, j):
                    inf += Grid.dist_cases((i, j), Grid.calcul_coordonnees(x, len(G), len(G[0])))
        return inf/2
        # renvoie une approximation de la distance entre la grille actuelle et le but

    def trouver_coord(self, k):  # trouve les coordonnées de k dans une grille
        for i in range(self.m):
            for j in range(self.n):
                if self.state[i][j] == k:
                    return (i, j)

    @staticmethod
    def dist_grilles(G, src):  # permet de claculer la distance entre la source et la grille
        # actuelle. Permet de calculer le coût
        dist = 0
        G = list(list(element) for element in G)
        for i in range(len(G)):
            for j in range(len(G[0])):
                if G[i][j] != src.state[i][j]:
                    dist += Grid.dist_cases((i, j), src.trouver_coord(G[i][j]))
        return dist

    def A_star(self, src, dst):
        noeuds_visites = []
        src_hash = tuple(tuple(element) for element in src.state)
        dst_hash = tuple(tuple(element) for element in dst.state)
        file = [(0, src_hash)]
        heapq.heapify(file)
        g = {}  # initialisation du graphe que l'on construit au fur et à mesure
        couts = {}
        couts[src_hash] = 0
        parents = {}
        while file:
            c, x = heapq.heappop(file)
            if x == dst_hash:
                break
            if x not in g:
                g[x] = []  # on construit le graphe au fur et à mesure
                for (i, j) in Grid.liste_noeuds_a_relier(self):
                    i1 = [list(t) for t in i]
                    j1 = [list(t) for t in j]
                    if x == i1:
                        g[x].append(j)
                    elif Grid.comp_mat(j1, x):
                        g[x].append(i)
            if x not in noeuds_visites:
                noeuds_visites.append(x)
            for voisin in g[x]:
                voisin_liste = list(list(x) for x in voisin)  # il faut retransformer en grid pour
                # pouvoir utiliser borne_inf_a_dst
                cout = Grid.dist_grilles(voisin, src) + Grid.borne_inf_a_dst(voisin_liste)
                # couts[voisin] = cout
                if voisin in noeuds_visites and couts[voisin] >= cout:
                    noeuds_visites.append(voisin)
                    parents[voisin] = x
                    heapq.heappush(file, (cout, voisin))
                    couts[voisin] = cout
                if voisin not in noeuds_visites:   # or (voisin in noeuds_visites and couts[voisin] >= cout):
                    noeuds_visites.append(voisin)
                    parents[voisin] = x
                    heapq.heappush(file, (cout, voisin))
                    couts[voisin] = cout
        chemin = [dst]  # on reconstitue le chemin parcouru pour arriver à la destination
        y = dst_hash
        while y != src_hash:
            # y = tuple(tuple(liste) for liste in y)
            y = parents[y]
            chemin = [y] + chemin
        chemin = [[list(t) for t in G] for G in chemin]
        return chemin



print Grid.


"""
    
    #gOrd =Grid.__init__(self,m , n , initial_state=[])
    #grille ordonnée



#class noeud():



    #def __init__(self,x, coût, heuristique, initial_state=[]):
     #       self.x=x
            self.coût=coût
            self.heuristique=heuristique
            if not initial_state:
                initial_state=[x, coût, heuristique]
            self.state = initial_state



    def A(self,src:noeud):
            src.coût=0
            closedList = Queue()
            openList = heapify([]) #liste de couples (valeur heuristique, noeud)
            heapq.heappush(openList, (0,src))
            parents={}
            g={}
            while openList:
                u=heapq.heappop(heap)[1]  #prend la valeur avec la plus petite heuristique
                if u==gOrd:
                    break
                for v in g[u]:
                    if not (v in closedList or (v in openList and (openList[0]<v.heuristique if openList[1]==v))):
                        v.coût = u.coût+1
                        v.heuristique = v.coût + (get_solution(self, m, n, v)/2)
                     #l'heuristique est la méthode naïve/2
                        heapq.heappush(openList, (v.heuristique,v))
                        parent[v]=u
                closedList.put(u)
            #maintenant on reconstitue le chemin
            chemin =[gOrd]
            y = g0rd
            while y != src:
                y =parents[y]
                chemin = [y] + chemin
            return chemin

"""
