from grid import Grid


def calcul_coordonnees(x, m, n):
    i = (x-1) // n
    j = (x-1) % n
    return (i, j)
    # cette fonction permet de déterminer les coordonnées d'un chiffre (compris entre 1 et m*n)
    # dans la grille


class Solver():

    """
      A solver class, to be implemented.
    """

    """
    Question 3

    -La fonction fonctionne quel que soit l'état initial de la grille.

    -Complexité en temps :
        - dans le meilleur des cas, si la grille est triée : (m*n)²
        - dans le pire des cas : (m+n)*(m*n)²  (ordre de grandeur)
            cette valeur est un peu surestimée car il faudra parcourir la boucle while m+n fois
            seulement pour les cases qui sont dans un coin et doivent être placées dans le coin
            opposé

    -ordre de grandeur du nombre d'opérations : celui-ci dépend de l'état initial de la grille.
        - il peut être très faible si la grille est presque triée (si elle ne nécessite que quelques
          swaps)
        - dans le pire des cas on peut imaginer que chaque case est à l'opposée de là où elle doit
         être. Par exemple pour mettre les premières cases à leur place on peut supposer qu'il
         faudra faire m+n swaps, puis pour la rangée du dessous m+n-2, et ainsi de suite
         ce qui correspond à n*(m+n)+n*(m+n-2)+n*(m+n-4)+...+n

    - La longueur n'est pas forcément optimale en allant chercher chaque nombre dans l'ordre
      croissant parce qu'il est possible que des swaps permettant d'emmener une case au bon
      endroit soient aussi utiles pour une autre case. Or ici comme on déplace chaque case sans
      prendre en compte les swaps qui ont été faits précedemment il est possible qu'on fasse
      plus de swaps que nécessaire.

    """

    def trouver(self, k, g):
        for i in range(g.m):
            for j in range(g.n):
                if g.state[i][j] == k:
                    return (i, j)
    # cette fonction permet de trouver un chiffre dans la grille, afin de connaître ses coordonnées,
    # pour ensuite savoir comment le déplacer jusqu'à la bonne place

    def get_solution(self, m, n, g):
        changements = []
        for k in range(1, m*n+1):
            i, j = calcul_coordonnees(k, m, n)
            while self.trouver(k, g) != (i, j):
                if self.trouver(k, g)[0] > i:
                    x = self.trouver(k, g)[0]  # on note x afin de raccourcir les lignes
                    changements.append((self.trouver(k, g), (x-1, self.trouver(k, g)[1])))
                    g.swap(self.trouver(k, g), (x-1, self.trouver(k, g)[1]))
                elif self.trouver(k, g)[0] < i:
                    x = self.trouver(k, g)[0]
                    changements.append((self.trouver(k, g), ((x)+1, self.trouver(k, g)[1])))
                    g.swap(self.trouver(k, g), ((x+1, self.trouver(k, g)[1])))
                if self.trouver(k, g)[1] > j:
                    x = self.trouver(k, g)[0]
                    changements.append((self.trouver(k, g), (x, self.trouver(k, g)[1]-1)))
                    g.swap(self.trouver(k, g), (x, self.trouver(k, g)[1]-1))
                elif self.trouver(k, g)[1] < j:
                    x = self.trouver(k, g)[0]
                    changements.append((self.trouver(k, g), (x, self.trouver(k, g)[1]+1)))
                    g.swap(self.trouver(k, g), (x, self.trouver(k, g)[1]+1))
        return changements

        """
        Solves the grid and returns the sequence of swaps at the format
         [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """


