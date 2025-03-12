from random import randint
import time


def creer_grille(x, y):
    grille = []
    for i in range(y):
        grille.append([])
        for j in range(x):
            grille[i].append(0)
    return grille


def hauteur_grille(grille):
    compteur = 0
    for elem in grille:
        compteur += 1
    return compteur


def largeur_grille(grille):
    compteur = 0
    for elem in grille[0]:
        compteur += 1
    return compteur


def creer_grille_aleatoire(x, y, p):
    grille = []
    for i in range(y):
        grille.append([])
        for j in range(x):
            proba = randint(0, 100)
            if proba < (p*100):
                grille[i].append(1)
            else:
                grille[i].append(0)
    return grille


def voisins_case(grille, x, y):
    voisins = []
    if x == 0 and y == 0:
        voisins.append(grille[y+1][x])
        voisins.append(grille[y+1][x+1])
        voisins.append(grille[y][x+1])
    elif x == 0 and y == hauteur_grille(grille) - 1:
        voisins.append(grille[y-1][x])
        voisins.append(grille[y-1][x+1])
        voisins.append(grille[y][x+1])
    elif x == largeur_grille(grille) - 1 and y == 0:
        voisins.append(grille[y+1][x])
        voisins.append(grille[y+1][x-1])
        voisins.append(grille[y][x-1])
    elif x == largeur_grille(grille) - 1 and y == hauteur_grille(grille) - 1:
        voisins.append(grille[y-1][x])
        voisins.append(grille[y-1][x-1])
        voisins.append(grille[y][x-1])
    elif x == 0 and 0 < y < hauteur_grille(grille) - 1:
        voisins.append(grille[y-1][x])
        voisins.append(grille[y-1][x+1])
        voisins.append(grille[y][x+1])
        voisins.append(grille[y+1][x+1])
        voisins.append(grille[y+1][x])
    elif 0 < x < largeur_grille(grille) - 1 and y == 0:
        voisins.append(grille[y][x-1])
        voisins.append(grille[y+1][x-1])
        voisins.append(grille[y+1][x])
        voisins.append(grille[y+1][x+1])
        voisins.append(grille[y][x+1])
    elif 0 < x < largeur_grille(grille) - 1 and y == hauteur_grille(grille) - 1:
        voisins.append(grille[y][x-1])
        voisins.append(grille[y-1][x-1])
        voisins.append(grille[y-1][x])
        voisins.append(grille[y-1][x+1])
        voisins.append(grille[y][x+1])
    elif x == largeur_grille(grille) - 1 and 0 < y < hauteur_grille(grille) - 1:
        voisins.append(grille[y-1][x])
        voisins.append(grille[y-1][x-1])
        voisins.append(grille[y][x-1])
        voisins.append(grille[y+1][x-1])
        voisins.append(grille[y+1][x])
    else:
        voisins.append(grille[y-1][x-1])
        voisins.append(grille[y-1][x])
        voisins.append(grille[y-1][x+1])
        voisins.append(grille[y][x-1])
        voisins.append(grille[y][x+1])
        voisins.append(grille[y+1][x-1])
        voisins.append(grille[y+1][x])
        voisins.append(grille[y+1][x+1])
    return voisins


def nb_cellules_voisines(grille, x, y):
    compteur = 0
    voisins = voisins_case(grille, x, y)
    for elem in voisins:
        if elem == 1:
            compteur += 1
    return compteur


def afficher_grille(grille):
    for ligne in grille:
        for cellule in ligne:
            if cellule == 0:
                print("_", end=" ")
            else:
                print("O", end=" ")
        print()
    return


def generation_suivante(grille):
    largeur = largeur_grille(grille)
    hauteur = hauteur_grille(grille)
    nouvelle_grille = creer_grille(largeur, hauteur)
    # Parcours de chaque cellule de la grille
    for i in range(hauteur_grille(grille)):
        for j in range(largeur_grille(grille)):
            nb_voisins = nb_cellules_voisines(grille, j, i)
            if grille[i][j] == 1:
                # La cellule reste vivante si elle a 2 ou 3 voisins vivants
                nouvelle_grille[i][j] = 1 if 2 <= nb_voisins <= 3 else 0
            else:
                # Une nouvelle cellule naît si elle a exactement
                # 3 voisins vivants
                nouvelle_grille[i][j] = 1 if nb_voisins == 3 else 0
    return nouvelle_grille


def evolution_n_generation(grille, n):
    afficher_grille(grille)
    print("\n")
    for i in range(n):
        time.sleep(1)
        grille = generation_suivante(grille)
        afficher_grille(grille)
        print("\n")
    return


grille = creer_grille_aleatoire(20, 20, 0.5)


evolution_n_generation(grille, 100)
