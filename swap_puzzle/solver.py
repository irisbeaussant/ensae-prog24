from grid import Grid


def calcul_coordonnees(x, m, n):
    i = x // n
    j = x % n -1
    return (i, j)
    # cette fonction permet de déterminer les coordonnées d'un chiffre (compris entre 1 et m*n)
    # dans la grille

class Solver():

    """
    A solver class, to be implemented.
    """

    """ 
    Question 3

    -cet algorithme ressemble à celui du tri par selection dans la mesure où on va chercher 
    d'abord le plus petit pour le mettre à la bonne place, plus le deuxième petit et ainsi 
    de suite. L'algorithme de tri à plat a une complexité quadratique.
    -ordre de grandeur du nombre d'opérations : celui-ci dépend de l'état initial de la grille.
        
    -La fonction fonctionne quel que soit l'état initial de la grille.
    -La longueur de chemin n'est cependant pas idéale puisqu'o

    """

    def trouver(self, k, g):
        for i in range(g.m):
            for j in range(g.n):
                if g.state[i][j] == k:
                    return (i, j)
    # cette fonction permet de trouver un chiffre dans la grille, afin de connaître ses coordonnées, pour ensuite savoir comment le déplacer jusqu'à la bonne place




    def get_solution(self, m, n, g):
        changements = []
        for k in range(1, m*n+1):
            i, j = calcul_coordonnees(k, m, n)
            while self.trouver(k, g) != calcul_coordonnees(k, g, n):
                if self.trouver(k, g)[0] > i:
                    x = self.trouver(k, g)[0]  # on note x afin de raccourcir les lignes
                    g.swap(self.trouver(k, g), ((x)-1, self.trouver(k, g)[1]))
                    changements.append((self.trouver(k, g), ((x)+1, self.trouver(k, g)[1])))
                elif self.trouver(k, g)[0] < i:
                    x = self.trouver(k, g)[0]
                    g.swap(self.trouver(k, g), ((x+1, self.trouver(k, g)[1])))
                    changements.append((self.trouver(k, g), ((x)-1, self.trouver(k, g)[1])))
                if self.trouver(k, g)[1] > j:
                    x = self.trouver(k, g)[0]
                    g.swap(self.trouver(k, g), ((x), self.trouver(k, g)[1]-1))
                    changements.append((self.trouver(k, g), ((x)-1, self.trouver(k)[1]-1)))
                elif self.trouver(k, g)[1] < j:
                    x = self.trouver(k, g)[0]
                    g.swap(self.trouver(k, g), ((x), self.trouver(k, g)[1]+1))
                    changements.append((self.trouver(k, g), ((x)-1, self.trouver(k, g)[1]+1)))
            return changements


        """
        Solves the grid and returns the sequence of swaps at the format
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
