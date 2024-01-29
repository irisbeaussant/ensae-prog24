from grid import Grid

class Solver(): 

    """
    A solver class, to be implemented.
    """
    
    def trouver(self,k):
        for i in range(self.m):
            for j in range(self.n):
                if self.state[i][j]==k:
                    return (i,j)
    #cette fonction permet de trouver un chiffre dans la grille, afin de connaître ses coordonnées, pour ensuite savoir comment le déplacer jusqu'à la bonne place

    def calcul_coordonnées(x,m,n):
        i=x//n
        j=x%n
        return (i,j)
    #cette fonction permet de déterminer les coordonnées d'un chiffre (compris entre 1 et m*n) dans la grille



    def get_solution(self,m,n):
        changements=[]
        for l in range (1, m*n+1):
            i1,j1=trouver(self,l)
            i,j=calcul_coordonnées(l,m,n)
            while trouver(self,l)!=calcul_coordonnees(l,m,n):
                if i1>i:
                    swap(self,trouver(self,l),((trouver(self,l)[0])-1,trouver(self,l)[1]))
                    changements.append((trouver(self,l),((trouver(self,l)[0])+1,trouver(self,l)[1])))
                elif i1<i:
                    swap(self,trouver(self,l),((trouver(self,l)[0])+1,trouver(self,l)[1]))
                    changements.append((trouver(self,l),((trouver(self,l)[0])-1,trouver(self,l)[1])))
                if j1>j:
                    swap(self,trouver(self,l),((trouver(self,l)[0]),trouver(self,l)[1]-1))
                    changements.append((trouver(self,l),((trouver(self,l)[0])-1,trouver(self,l)[1]-1)))
                elif j1<j:
                    swap(self,trouver(self,l),((trouver(self,l)[0]),trouver(self,l)[1]+1))
                    changements.append((trouver(self,l),((trouver(self,l)[0])-1,trouver(self,l)[1]+1))) 
            return changements

        """
        La fonction fonctionne quel que soit l'état initial de la grille.
        La longueur de chemin n'est cependant pas idéale 
        """


        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        raise NotImplementedError

