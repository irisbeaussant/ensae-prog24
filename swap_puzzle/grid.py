from itertools import permutations
import numpy as np
import random
from itertools import permutations
import matplotlib.pyplot as plt
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
        for i in range(len(self.state)):
            for j in range(len(self.state[0])):
                plt.text(j, i, str(self.state[i][j]))
        plt.colorbar()
        plt.show()
        
    def representation_graphique_bis(self):  # représentation sous la forme d'un tableau
        grille = self.state

        fig, ax = plt.subplots()

        taille_case = 0.3

        ax.set_axis_off()
        tableau = ax.table(cellText=grille, cellLock='center')
        tableau.scale(1, 1)

        for texte, case in tableau.get_celld().items():
            case.set_height(taille_case)
            case.set_width(taille_case)
        plt.show()

    """
    Question 6 :

    Les noeuds sont de type hashable donc il faut transformer chaque grille en un élément non
    mutable, on les transforme en tuples.

    Afin de créer toutes les grilles possibles on trouve toutes les permutations.

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
    il faut le construire au fur et à mesure de son parcours.
    
    """

    @staticmethod
    def liste_noeuds_a_relier_bis(grille):  # prend en argument une liste de listes
        m = len(grille)
        n = len(grille[0])
        L = []  # on initialise la liste des noeuds qui sont des voisins de la grille qu'on étudie
        for i in range(m):   # au lieu de parcourir tous les noeuds et de vérifier s'il sont des
            # voisins de la grille on va construire tous les voisins. Cela évite d'avoir à comparer
            # des grilles.
            for j in range(n):
                if (i-1) >= 0:
                    G = np.copy(grille)
                    G[i][j], G[i-1][j] = G[i-1][j], G[i][j]
                    L.append(G)
                if (i+1) <= (m-1):
                    G = np.copy(grille)
                    G[i][j], G[i+1][j] = G[i+1][j], G[i][j]
                    L.append(G)
                if (j-1) >= 0:
                    G = np.copy(grille)
                    G[i][j], G[i][j-1] = G[i][j-1], G[i][j]
                    L.append(G)
                if (j+1) <= (n-1):
                    G = np.copy(grille)
                    G[i][j], G[i][j+1] = G[i][j+1], G[i][j]
                    L.append(G)
        return L
        # renvoie la liste des voisins
                  
    def bfs_bis(self, src, dst):
        file = Queue()
        src_hash = tuple(tuple(element) for element in src.state)
        dst_hash = tuple(tuple(element) for element in dst.state)
        file.put(src_hash)
        sommets_visites = []
        parents = {}  # est un dictionnaire du type {sommet : voisin parcouru juste avant}
        g = {}  # on initialise le dictionnaire du graphe
        while file:
            x = file.get()
            if x == dst_hash:
                break
            if x not in sommets_visites:
                sommets_visites.append(x)
            if x not in g:
                g[x] = []  # on construit le graphe au fur et à mesure
                x_l = list(list(element) for element in x)
                for i in Grid.liste_noeuds_a_relier_bis(x_l):
                    i = tuple(tuple(element) for element in i)  # la liste de noeuds voisins de x
                    # est une liste de liste de listes. Il faut donc les retransformer en des tuples
                    # afin d'avoir des variables hashables
                    if i not in g[x]:
                        g[x].append(i)
            for voisin in g[x]:
                if voisin not in sommets_visites:
                    file.put(voisin)
                    parents[voisin] = x
                    sommets_visites.append(voisin)
        chemin = [dst_hash]
        y = dst_hash
        while y != src_hash:
            y = parents[y]
            chemin = [y] + chemin
        chemin = [[list(t) for t in G] for G in chemin]
        return chemin

    """
    Algorithme A*

    heuristiques:

    - somme des distances des cases de la grille à leur bonne position (distance manhattan), le tout divisé par 2.
    La division par 2 permet d'avoir une estimation qui soit inférieure au nombre de swaps qu'il 
    faut réellement. En effet lorsqu'on échange 2 cases il ne faut qu'un swap
    C'est cette heuristique qui est utilisée dans le code si dessous.

    - on pourrait utiliser cette même somme mais prendre la racine carrée au lieu de diviser par 2

    - on pourrait calculer la somme des distance euclidiennes mais cela ne paraît pas très adapté
    car on ne peut pas réaliser de swaps en diagonale

    - on pourrait calculer le nombre de cases mal placées. En effet plus le nombre de cases mal 
    placées est grand plus le coût serait grand.

    """

    @staticmethod
    def calcul_coordonnees(x, m, n):  # calcule les coordonnées qu'une certaine case est censée avoir
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
    def borne_inf_a_dst(G):  # heuristique
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

    def A_star(self, src, dst):
        noeuds_visites = []
        src_hash = tuple(tuple(element) for element in src.state)
        dst_hash = tuple(tuple(element) for element in dst.state)
        file = [(0, src_hash)]
        heapq.heapify(file)
        dist_a_la_source = {src_hash: 0}
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
                x_l = list(list(element) for element in x)
                for i in Grid.liste_noeuds_a_relier_bis(x_l):
                    i_bis = tuple(tuple(element) for element in i)  # la liste de noeuds
                    # voisins de x est une liste de liste de listes. Il faut donc les                     
                    # retransformer en des tuples afin d'avoir des variables hashables
                    if i_bis not in g[x]:
                        g[x].append(i_bis)
            if x not in noeuds_visites:
                noeuds_visites.append(x)
            for voisin in g[x]:
                dist_a_la_source[voisin] = dist_a_la_source[x]+1
                voisin_liste = list(list(x) for x in voisin)  # il faut retransformer en grid pour
                # pouvoir utiliser borne_inf_a_dst
                cout = dist_a_la_source[voisin] + Grid.borne_inf_a_dst(voisin_liste)
                if voisin in noeuds_visites and couts[voisin] >= cout:
                    noeuds_visites.append(voisin)
                    parents[voisin] = x
                    heapq.heappush(file, (cout, voisin))
                    couts[voisin] = cout
                if voisin not in noeuds_visites:
                    noeuds_visites.append(voisin)
                    parents[voisin] = x
                    heapq.heappush(file, (cout, voisin))
                    couts[voisin] = cout
        chemin = [dst_hash]  # on reconstitue le chemin parcouru pour arriver à la destination
        y = dst_hash
        while y != src_hash:
            y = tuple(tuple(liste) for liste in y)
            y = parents[y]
            chemin = [y] + chemin
        chemin = [[list(t) for t in G] for G in chemin]
        return chemin

    # swaps_A_star complète le résultat de chemin_le_plus_court en renvoyant les swaps nécessaires
    # pour réaliser ce chemin

    def swaps_A_star(self, etatinitial, etatfinal):
        liste_grilles = Grid.A_star(self, etatinitial, etatfinal)
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
    5_ barrières

    On crée des barrières pour complexifier le problème.

    """

    # La fonction sep_par_barrieres prend en argument deux grilles voisines et la liste des
    # barrières.
    # Elle vérifie si le swap qui permet de passer d'une grille à l'autre est autorisé
    # ou s'il y a une barrière qui l'empêche.

    def sep_par_barriere(grille1, grille2, barrieres):
        # barrières est une liste de listes. Chaque sous-liste est composée de quatre
        # chiffres p, q, r, s tels que les coordonnées de la case d'un côté de la barrière
        # sont (p,q) et que les coordonnées de la case de l'autre côté de la barrière
        # sont (r,s)
        for i in barrieres:
            p, q = i[0], i[1]  # coordonnées de la case d'un côté de la barrière
            r, s = i[2], i[3]  # coordonnées de la case de l'autre côté de la barrière
            if grille1[p][q] == grille2[r][s]:  # i.e. il faut effectuer un swap entre les
                # cases de coordonnées (p,q) et (r,s) pour passer d'une grille à l'autre
                return False  # False signifie que le swap est interdit, il y a une barrière
        return True
        # True signifie qu'on a le droit de faire le swap

    def barrieres(self, src, dst, barrieres):
        noeuds_visites = []
        src_hash = tuple(tuple(element) for element in src.state)
        dst_hash = tuple(tuple(element) for element in dst.state)
        file = [(0, src_hash)]
        heapq.heapify(file)
        dist_a_la_source = {src_hash: 0}
        g = {}  # initialisation du graphe que l'on construit au fur et à mesure
        couts = {}
        couts[src_hash] = 0
        parents = {}
        while file:
            c, x = heapq.heappop(file)
            print("x=", x)
            if x == dst_hash:
                break
            if x not in g:
                g[x] = []  # on construit le graphe au fur et à mesure
                x_l = list(list(element) for element in x)
                for i in Grid.liste_noeuds_a_relier_bis(x_l):
                    i_bis = tuple(tuple(element) for element in i)  # la liste de noeuds
                    # voisins de x est une liste de liste de listes. Il faut donc les                 
                    # retransformer en des tuples afin d'avoir des variables hashables
                    if not g[x]:
                        g[x].append(i_bis)
                        # si g[x] est vide on ne pourra pas rentrer dans la boucle for qui suit
                    for j in g[x]:
                        if not Grid.comp_mat(i, list(list(element) for element in j)):
                            # on vérifie que i n'est pas déjà dans la liste des voisins de g
                            if Grid.sep_par_barriere(i, x_l, barrieres):
                                # i.e. si on peut faire le swap
                                g[x].append(i_bis)
            if x not in noeuds_visites:
                noeuds_visites.append(x)
            for voisin in g[x]:
                dist_a_la_source[voisin] = dist_a_la_source[x]+1
                voisin_liste = list(list(x) for x in voisin)  # il faut retransformer en grid
                # pour pouvoir utiliser borne_inf_a_dst
                cout = dist_a_la_source[voisin] + Grid.borne_inf_a_dst(voisin_liste)
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
        chemin = [dst_hash]  # on reconstitue le chemin parcouru pour arriver à la destination
        y = dst_hash
        while y != src_hash:
            y = tuple(tuple(liste) for liste in y)
            y = parents[y]
            chemin = [y] + chemin
        chemin = [[list(t) for t in G] for G in chemin]
        return chemin

    """
    6_ cas particuliers et algorithmes
      
     - si on a une grille 1*n on se retrouve à devoir trier une liste. Il existe de nombreux
    algorithmes de tri dans ce cas. On peut par exemple effectuer un tri à bulles, qui trie
    la liste en comparant 2 par 2 les cases et en faisant à chque boucle remonter le plus
    grand nombre.
    Il faut un tri où on n'échange que des cases qui se touchent, donc pas un tri par sélection par 
    exemple

    """
            
    def tri_bulles(self):
        L = self.state
        swaps = []
        if len(self.state) != 1:
            return ("le grille doit être de taille 1*n")
        n = self.n
        for i in range(n):
            for j in range(n-i-1):  # au fur et à mesure que l'algorithme se déroule
                # la fin de la liste devient triée, il est donc inutile de comparer 
                if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
                    swaps.append((L(j), L(j+1)))
        return swaps

    """
    Choix de la difficulté de la grille
    """
    def difficulte(self, difficulte):  # difficulte doit valoir 1, 2 ou 3
        m = self.m
        n = self.n
        if difficulte == 1:
            nombre_swaps = min(m, n)
        if difficulte == 2:
            nombre_swaps = m+n
        if difficulte == 3:
            nombre_swaps = 2*(m+n)
        for i in range(nombre_swaps):
            x = random.randint(0, n-1)
            y = random.randint(0, m-1)
            depl = random.randint(0, 1)  # 0 pour un déplacement vers la gauche ou vers le bas,
            # 1 vers la droite ou vers le haut
            x_ou_y = random.randint(0, 1)  # 0 pour un déplacement vertical, 1 pour un
            # déplacement horizontal
            if x_ou_y == 0:
                if depl == 0:
                    if x-1 >= 0:
                        Grid.swap(self, (x, y), (x-1, y))
                elif depl == 1:
                    if x+1 <= n-1:
                        Grid.swap(self, (x, y), (x+1, y))            
            if x_ou_y == 0:
                if depl == 0:
                    if y-1 >= 0:
                        Grid.swap(self, (x, y), (x, y-1))
                if depl == 1:
                    if y+1 <= m-1:
                        Grid.swap(self, (x, y), (x, y+1))