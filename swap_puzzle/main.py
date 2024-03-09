from grid import Grid


g = Grid(2, 3)
print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)


"""
    UTILISATION DES DIFFERENTES FONCTIONS

    Le fichier graph.py contient:

        - la fonction bfs(self, src, dst) qui utilise la méthode BFS pour des 
        graphes de nombres

    Le fichier grid.py contient les fonctions:

        - is_sorted(self)
        - swap(self, cell1, cell2)
        - swap_seq(self, cell_pair_list)
        - representation_graphique(self)
        - representation_graphique_bis(self)
        - noeuds(self) --> renvoie toutes les grilles possibles de la bonne taille
        - liste_noeuds_a_relier(self) --> renvoie la liste des couples de grilles voisines
        - liste_noeuds_a_relier_bis(grille) --> renvoie la liste des voisins de grille
        - chemin_le_plus_court(self, src, dst) --> BFS pour des grilles
        - swaps_a_faire(self, src, dst) --> renvoie les swaps à faire pour réaliser le chemin que renvoie la fonction précédente
        - bfs_bis(self, src, dst) --> bfs avec construction du graphe au fur et à mesure
        - borne_inf_a_dst(G) --> renvoie l'heuristique
        - A_star(self, src, dst)
        - swaps_A_star(self, src, dst) --> renvoie les swaps à faire pour réaliser le chemin que renvoie A_star
        - sep_par_barriere(grille1, grille2, barrieres) --> renvoie False si on ne peut pas effecter le swap entre ces deux grilles voisines à cause d'une barrière, True sinon
        - barrieres(self, src, dst, barrieres) --> renvoie le chemin pour passer de src à dst étant données des barrières
        - tri_bulles(self)

    Le fichier solver.py contient:

        - la fonction get_solution(self, m, n, g) --> renvoie la solution naïve

"""