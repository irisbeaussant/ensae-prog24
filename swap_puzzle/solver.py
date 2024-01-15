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


    def get_solution(self):
        for k in range(self.n*self.m):
            if trouver(self,k)[1]>
            




        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        raise NotImplementedError

