from grid import Grid

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

    def trouver(self, k):
        for i in range(Grid.m):
            for j in range(Grid.n):
                if self.state[i][j] == k:
                    return (i, j)
    # cette fonction permet de trouver un chiffre dans la grille, afin de connaître ses coordonnées, pour ensuite savoir comment le déplacer jusqu'à la bonne place

    def calcul_coordonnées(x, m, n):
        i = x // n
        j = x % n
        return (i, j)
    # cette fonction permet de déterminer les coordonnées d'un chiffre (compris entre 1 et m*n) 
    # dans la grille


    def get_solution(self, m, n):
        changements = []
        for l in range(1, m*n+1):
            i1, j1 = Solver.trouver(self, l)
            i, j = Solver.calcul_coordonnées(l, m, n)
            while Solver.trouver(l) != Solver.calcul_coordonnees(l, m, n):
                if i1 > i:
                    Grid.swap(Solver.trouver(l), ((Solver.trouver(self, l)[0])-1, Solver.trouver(l)[1]))
                    changements.append((Solver.trouver(l), ((Solver.trouver(l)[0])+1, Solver.trouver(l)[1])))
                elif i1 < i:
                    Grid.swap(Solver.trouver(l), ((Solver.trouver(l)[0])+1, Solver.trouver(l)[1]))
                    changements.append((Solver.trouver(l), ((Solver.trouver(l)[0])-1, Solver.trouver(l)[1])))
                if j1 > j:
                    Grid.swap(Solver.trouver(l), ((Solver.trouver(l)[0]), Solver.trouver(self, l)[1]-1))
                    changements.append((Solver.trouver(l), ((Solver.trouver(l)[0])-1, Solver.trouver(l)[1]-1)))
                elif j1 < j:
                    Grid.swap(Solver.trouver(l), ((Solver.trouver(l)[0]), Solver.trouver(l)[1]+1))
                    changements.append((Solver.trouver(l), ((Solver.trouver(l)[0])-1, Solver.trouver(l)[1]+1))) 
            return changements


        """
        Solves the grid and returns the sequence of swaps at the format
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing 
        # imposed is the format of the solution returned.
        raise NotImplementedError

