# import numpy as np
# plateau=np.array([[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,1,1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,-1],[-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1],[-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1],[-1,1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]])
# 
# 
# 
# 
# plateau_simplifie=np.array([[0,1,1,1,1,0],
#                             [1,1,1,1,1,1],
#                             [0,1,0,0,1,0],
#                             [0,1,0,0,1,0],
#                             [1,1,1,1,1,1],
#                             [0,0,1,1,0,0]])
#                             
#                             
# def pacman():
# 
#     compteur=0
#     position_pacman=[11,14]
#     plateau[position_pacman[0]][position_pacman[1]] = 2
#     deplacements={"haut":[-1,0], "bas":[1,0], "droite":[0,+1], "gauche":[0,-1]}
#     print(plateau_simplifie)
#     while condition_victoire(compteur) :
#         deplacement = input("deplacement?\n")
#         case_depart = position_pacman
#         case_arrivee = [position_pacman[0]+deplacements[deplacement][0],position_pacman[1]+deplacements[deplacement][1]]
#         if plateau[case_arrivee[0]][case_arrivee[1]] == 1:
#             # compteur += plateau_simplifie[case_arrivee[0]][case_arrivee[1]]
#             plateau[case_depart[0]][case_depart[1]][1] = 0
#             position_pacman = case_arrivee
#         # elif plateau[case_arrivee[0]][case_arrivee[1]][0] == -1:
#         #     plateau_simplifie[case_depart[0]][case_depart[1]] = 2
#         #     position_pacman = case_arrivee
#         plateau[position_pacman[0]][position_pacman[1]][1] = 2
#         print(plateau_simplifie)
#     print( "BIEN JOUE PETIT CHENAPANT")
#         
#     
# 
# def condition_victoire(compteur):
#     if compteur == 22:
#         return False
#     return True
# 
# [1,0]
# [-1,0]
# [1,2]
# 

##2
import time as t
import numpy as np
plateau=np.matrix([[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,1,1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,-1],[-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1],[-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1],[-1,1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]])

MUR = -1
VIDE = 0
FRUIT = 1
PACMAN = 8
    
    # 
    # plateau_simplifie=np.array([[0,1,1,1,1,0],
    #                             [1,1,1,1,1,1],
    #                             [0,1,0,0,1,0],
    #                             [0,1,0,0,1,0],
    #                             [1,1,1,1,1,1],
    #                             [0,0,1,1,0,0]])
                                
                                
def pacman():
    plateau=np.matrix([[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,1,1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,-1],[-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1],[-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1],[-1,1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]])

    compteur=0
    coup = 0
    vie = 3
    position_pacman=[17,14]
    position_fantome_1=[1,1]
    valeur_precedente_1 = plateau[position_fantome_1[0],position_fantome_1[1]]
    plateau[position_pacman[0],position_pacman[1]]=8
    plateau[position_fantome_1[0],position_fantome_1[1]]=10
    print(afficher_plateau_lisible(plateau))
    while condition_victoire(compteur) and vie != 0 :

        chemin_f1 = fantome_1([position_fantome_1],plateau)
        case_f1 = chemin_f1[0]
        plateau[position_fantome_1[0], position_fantome_1[1]] = valeur_precedente_1
        valeur_precedente_1 = plateau[case_f1[0], case_f1[1]]
        plateau[case_f1[0], case_f1[1]] = 10
        position_fantome_1 = case_f1

        if position_fantome_1 == position_pacman:
            vie += -1
            chemin_pac = diffusion([position_pacman], plateau)
            for k in range(5):
                case_arrivee = chemin_pac[k]
                compteur += plateau[case_arrivee[0], case_arrivee[1]]
                plateau[position_pacman[0], position_pacman[1]] = 0
                plateau[case_arrivee[0], case_arrivee[1]] = 8
                position_pacman = case_arrivee
                coup += 1
            continue

        chemin_pac = diffusion([position_pacman],plateau)
        for k in range(2):
            case_arrivee = chemin_pac[k]
            compteur += plateau[case_arrivee[0], case_arrivee[1]]
            plateau[position_pacman[0], position_pacman[1]] = 0
            plateau[case_arrivee[0], case_arrivee[1]] = 8
            position_pacman = case_arrivee
            coup += 1
            t.sleep(1)
            print(afficher_plateau_lisible(plateau))

    print( "BIEN JOUE PETIT CHENAPANT", coup, afficher_plateau_lisible(plateau) )
        
    

def condition_victoire(compteur):
    if compteur == 252:
        return False
    return True





def afficher_plateau_lisible(plateau):
    chars = {MUR: 'X', VIDE: '0', FRUIT: '.', PACMAN: 'G'}
    height, width = np.shape(plateau)
    return '\n'.join([
        ''.join([chars[plateau[i, j]] for j in range(width)])
        for i in range(height)
    ])
#     plateau_bis=plateau
#     for k in range(31):
#         for i in range(28):
#             if plateau[k][i]==-1:
#                 plateau_bis[k][i]='X'
#             elif plateau[k][i]==1:
#                 plateau_bis[k][i]='.'
#             elif plateau[k][i]==0:
#                 plateau_bis[k][i]='O'
#     return plateau_bis
# compteur=0    
# for k in range(31):
#     for i in range(28):
#         if plateau[k,i]==8:
#             print([k,i])

[1,0]
[-1,0]
[1,2]
## parcours par recherche du point le plus proche et recherche de chemin par diffusion

def recherche_point_le_plus_proche(position_pacman,plateau):
    case_etudier = position_pacman
    point = plateau[ case_etudier[0], case_etudier[1] ]
    if point == 1:
        return case_etudier
    elif point == -1:
        return "erreur"
    elif point == 0 or point == 8:
        bas = recherche_point_le_plus_proche_bas([ case_etudier[0]+1, case_etudier[1]],plateau)
        if bas != "erreur":
            return bas
        haut = recherche_point_le_plus_proche_haut([ case_etudier[0]-1, case_etudier[1]],plateau)
        if haut != "erreur":
            return haut
        droite = recherche_point_le_plus_proche_droite([ case_etudier[0], case_etudier[1]+1],plateau)
        if droite != "erreur":
            return droite
        gauche = recherche_point_le_plus_proche_gauche([ case_etudier[0], case_etudier[1]-1],plateau)
        if gauche !=  "erreur":
            return gauche
            
        
        
def recherche_point_le_plus_proche_bas(liste_coup,plateau):
    case_etudier = liste_coup[-2:]
    point = plateau[ case_etudier[0], case_etudier[1] ]
    if point == 1:
        return case_etudier
    elif point == -1:
        return "erreur"
    elif point == 0 or point == 8:
        bas = recherche_point_le_plus_proche_bas([ case_etudier[0]+1, case_etudier[1]],plateau)
        if bas != "erreur":
            return liste_coup+bas
        # haut = recherche_point_le_plus_proche([ case_etudier[0]-1, case_etudier[1]],plateau)
        # if haut != "erreur":
        #     return haut
        droite = recherche_point_le_plus_proche_droite([ case_etudier[0], case_etudier[1]+1],plateau)
        if droite != "erreur":
            return liste_coup+droite
        gauche = recherche_point_le_plus_proche_gauche([ case_etudier[0], case_etudier[1]-1],plateau)
        if gauche !=  "erreur":
            return liste_coup+gauche


def recherche_point_le_plus_proche_haut(liste_coup,plateau):
    case_etudier = liste_coup[-2:]
    point = plateau[ case_etudier[0], case_etudier[1] ]
    if point == 1:
        return case_etudier
    elif point == -1:
        return "erreur"
    elif point == 0 or point == 8:
        # bas = recherche_point_le_plus_proche([ case_etudier[0]+1, case_etudier[1]],plateau)
        # if bas != "erreur":
        #     return bas
        haut = recherche_point_le_plus_proche_haut([ case_etudier[0]-1, case_etudier[1]],plateau)
        if haut != "erreur":
            return liste_coup+haut
        droite = recherche_point_le_plus_proche_droite([ case_etudier[0], case_etudier[1]+1],plateau)
        if droite != "erreur":
            return liste_coup+droite
        gauche = recherche_point_le_plus_proche_gauche([ case_etudier[0], case_etudier[1]-1],plateau)
        if gauche !=  "erreur":
            return liste_coup+gauche
            
    
def recherche_point_le_plus_proche_gauche(liste_coup,plateau):
    case_etudier = liste_coup[-2:]
    point = plateau[ case_etudier[0], case_etudier[1] ]
    if point == 1:
        return case_etudier
    elif point == -1:
        return "erreur"
    elif point == 0 or point == 8:
        bas = recherche_point_le_plus_proche_bas([ case_etudier[0]+1, case_etudier[1]],plateau)
        if bas != "erreur":
            return liste_coup+bas
        haut = recherche_point_le_plus_proche_haut([ case_etudier[0]-1, case_etudier[1]],plateau)
        if haut != "erreur":
            return liste_coup+haut
        # droite = recherche_point_le_plus_proche([ case_etudier[0], case_etudier[1]+1],plateau)
        # if droite != "erreur":
        #     return droite
        gauche = recherche_point_le_plus_proche_gauche([ case_etudier[0], case_etudier[1]-1],plateau)
        if gauche !=  "erreur":
            return liste_coup+gauche        
            
def recherche_point_le_plus_proche_droite(liste_coup,plateau):
    case_etudier = liste_coup[-2:]
    point = plateau[ case_etudier[0], case_etudier[1] ]
    if point == 1:
        return case_etudier
    elif point == -1:
        return "erreur"
    elif point == 0 or point == 8:
        bas = recherche_point_le_plus_proche_bas([ case_etudier[0]+1, case_etudier[1]],plateau)
        if bas != "erreur":
            return liste_coup+bas
        haut = recherche_point_le_plus_proche_haut([ case_etudier[0]-1, case_etudier[1]],plateau)
        if haut != "erreur":
            return liste_coup+haut
        droite = recherche_point_le_plus_proche_droite([ case_etudier[0], case_etudier[1]+1],plateau)
        if droite != "erreur":
            return liste_coup+droite
        # gauche = recherche_point_le_plus_proche([ case_etudier[0], case_etudier[1]-1],plateau)
        # if gauche !=  "erreur":
        #     return gauche            
        #     
        
         # while point == 0:
         #    for _ in range(2):
         #        case_etudier[0] += -1
         #        point += plateau[ case_etudier[0], case_etudier[1] ]
         #        if point == 1:
         #            return 
                
                
                
# faire programme comme l'année derniere pour le déplacement entre 2 intersections
deplacements={"h":[-1,0], "b":[1,0], "d":[0,+1], "g":[0,-1]}




B=np.matrix([[-1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.],
        [-1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  -1.],
        [-1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1., 0.,  -1.],
        [-1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  -1.],
        [-1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  -1.],
        [-1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  -1.],
        [-1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  -1.],
        [-1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  -1.],
        [-1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  -1.],
        [-1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  -1.],
        [-1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  -1.],
        [-1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  -1.],
        [-1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  -1.],
        [-1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  -1.],
        [-1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.]])


plateau_test=np.matrix([[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,1,1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,0,0,0,0,8,0,0,0,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1],[-1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,1,1,-1],[-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1],[-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1],[-1,1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1],[-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1],[-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]])


def diffusion(liste_cases_etudiees,carte):
    liste_cases_future = []
    plateau = carte.copy()
    for case_precedente in liste_cases_etudiees:
        for deplacement in [[1,0],[-1,0],[0,1],[0,-1]]:
            case_suivante = np.array(case_precedente) + np.array(deplacement)
            if plateau[case_suivante[0],case_suivante[1]] == 0:
                plateau[case_suivante[0],case_suivante[1]] = 2
                liste_cases_future.append(case_suivante)
            elif plateau[case_suivante[0],case_suivante[1]] == 1:
                for case_remplie in liste_cases_future:
                    plateau[case_remplie[0],case_remplie[1]] = 0
                return [case_suivante]               #pareil qu'en bas
    # print(plateau)
    # t.sleep(1)
            
    chemin_retour = diffusion(liste_cases_future,plateau)  #rajouter ,carte pour voire
    # plateau = carte.copy()
    for deplacement in [[1,0],[-1,0],[0,1],[0,-1]]:
        case_precedente = np.array(chemin_retour[0]) + np.array(deplacement)
        if plateau[case_precedente[0],case_precedente[1]] == 2:
            for case_remplie in liste_cases_future:
                # if plateau[case_remplie[0],case_remplie[1]] == 2:
                plateau[case_remplie[0],case_remplie[1]] = 0 #indenter pour voire
            # plateau[case_precedente[0],case_precedente[1]] = 8
            chemin_retour.insert(0,case_precedente)
            # print(plateau)
            # t.sleep(1)
            return chemin_retour            #rajouter plateau pour voire la recherche
    
        
    
def fantome_1(liste_cases_etudiees, carte):
    liste_cases_future = []
    plateau = carte.copy()
    for case_precedente in liste_cases_etudiees:
        for deplacement in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            case_suivante = np.array(case_precedente) + np.array(deplacement)
            if plateau[case_suivante[0], case_suivante[1]] == 0:
                plateau[case_suivante[0], case_suivante[1]] = 2
                liste_cases_future.append(case_suivante)
            elif plateau[case_suivante[0], case_suivante[1]] == 8:
                for case_remplie in liste_cases_future:
                    plateau[case_remplie[0], case_remplie[1]] = 0
                return [case_suivante]

    chemin_retour = diffusion(liste_cases_future, plateau)
    for deplacement in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        case_precedente = np.array(chemin_retour[0]) + np.array(deplacement)
        if plateau[case_precedente[0], case_precedente[1]] == 2:
            for case_remplie in liste_cases_future:
                plateau[case_remplie[0], case_remplie[1]] = 0
            chemin_retour.insert(0, case_precedente)
            return chemin_retour

    


# liste_cases_etudiees = [[4,11]]
# liste_cases_future = []
# for case_precedente in liste_cases_etudiees:
#     print(case_precedente)
#     for deplacement in [[1,0],[-1,0],[0,1],[0,-1]]:
#         case_suivante = np.array(case_precedente) + np.array(deplacement)
#         if B[case_suivante[0],case_suivante[1]] == 0:
#             B[case_suivante[0],case_suivante[1]] += 2
#             liste_cases_future.append(case_suivante)
# print(liste_cases_future)
# print(B)

# 
# def test():
#     cc= [5,2]
#     ca= [6,9]
#     return [cc,ca]
#     
# def test2():
#     cz= [2,1]
#     cr =test()
#     cr.append(cz)
#     return cr









