"""
Auteur : Lorenzo OTTAVIANI
Date : 16/04/2024
But du programme :
    Le programme dessine le plan du château dans lequel on jouera le jeu.
Entrée : Fichier contenant le plan du château sous forme de matrice numérique.
Sortie : Dessin du plan de château via le module turtle.
"""
import turtle
from CONFIGS import *


def lire_matrice(fichier):
    """
    Lis sous forme de matrice le fichier contenant les caractéristiques de chacune des cases du château.
    :param fichier: Contient les caractéristiques de chaque case codée sous forme numérique.
    :return: Matrice numérique du plan du château.
    """
    with open(fichier) as file:
        return [[int(colonne) for colonne in ligne.split()] for ligne in file]


def bordures():
    """
    Dessine les limites des trois zones de l'écran (zone du plan du château, zone de l'inventaire, zone des annonces).
    :return: Retourne un écran divisé en trois zones.
    """
    turtle.color("black")
    turtle.up()
    turtle.goto(-240, 240)  # Dessine la zone des annonces.
    turtle.down()
    for i in range(2):
        turtle.forward(480)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
    turtle.up()
    turtle.goto(240, 210)  # Dessine la zone de l'inventaire.
    turtle.down()
    for j in range(2):
        turtle.right(90)
        turtle.forward(450)
        turtle.right(90)
        turtle.forward(170)
    turtle.up()
    turtle.goto(-240, -240)  # Dessine la zone du plan du château.
    turtle.down()
    for k in range(2):
        turtle.forward(290)
        turtle.left(90)
        turtle.forward(440)
        turtle.left(90)


def afficher_plan(matrice):
    """
    Dessine le plan du château à partir de sa matrice en utilisant le module turtle.
    :param matrice: Matrice numérique du plan du château
    :return: Dessin du plan de château via le module turtle
    """

    def calculer_pas(matrice):
        """
        Calcule la taille (en "pixels turtle") à donner à une case du plan, pour que le plan dans son ensemble
        tienne dans un rectangle de 290 de longueur (lignes) et 440 de hauteur (colonnes).
        :param matrice: Matrice numérique du plan du château
        :return: Taille maximale que peut avoir une case du plan (longueur de son côté, cases carrés).
        """
        pas_col = 440 // len(matrice)
        pas_lig = 290 // len(matrice[0])
        if pas_col <= pas_lig:
            pas = pas_col
        else:
            pas = pas_lig
        return pas

    def coordonnees(case, pas):
        """
        Calcule les coordonnées du coin inférieur gauche d'une case du plan (en "pixels turtle").
        :param case: Tuple identifiant la case du chateau. Les tuples identifiant les cases commencent avec (0,0)
        et sont de la forme (numéro des colonnes de haut en bas, numéro des lignes de gauche à droite).
        :param pas: Taille des cases du plan (longueur de son côté, cases carrés).
        :return: Coordonnées du côté inférieur gauche de la case.
        """
        cord = (-240 + case[1] * pas, 200 - (case[0] + 1) * pas)
        return cord

    def tracer_case(case, couleur, pas):
        """
        Trace une case d'une couleur et d'une taille choisie.
        :param case: Tuple identifiant la case du chateau par ses coordonnées en pixels turtle.
        :param couleur: Couleur de la case.
        :param pas: Taille des cases du plan (longueur de son côté, cases carrés).
        :return: Dessin de la case du plan.
        """

        def tracer_carre(dimension):
            """
                Trace un carré qui déssine les limites d'une case du plan.
                :param dimension: Taille des cases du plan (longueur de son côté, cases carrés).
                :return: Carré délimitant une case du plan.
            """
            for c in range(4):
                turtle.forward(dimension)
                turtle.left(90)

        turtle.up()
        turtle.goto(coordonnees(case, pas))
        turtle.down()
        turtle.color("white", couleur)
        turtle.begin_fill()
        tracer_carre(pas)
        turtle.end_fill()

    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] == 0:
                col = COULEURS[0]
            elif matrice[i][j] == 1:
                col = COULEURS[1]
            elif matrice[i][j] == 2:
                col = COULEURS[2]
            elif matrice[i][j] == 3:
                col = COULEURS[3]
            elif matrice[i][j] == 4:
                col = COULEURS[4]
            tracer_case((i, j), col, calculer_pas(matrice))
    turtle.done()


bordures()
afficher_plan(lire_matrice(fichier_plan))  # Dessine le plan du château.
