import tkinter as tk
import random

TAILLE_CELLULE = 10
LARGEUR_GRILLE = 80
HAUTEUR_GRILLE = 60

def creer_fenetre():
    racine = tk.Tk()
    racine.title("Jeu de la Vie")
    toile = tk.Canvas(racine, width=LARGEUR_GRILLE * TAILLE_CELLULE, height=HAUTEUR_GRILLE * TAILLE_CELLULE, bg="white")
    toile.pack()

    grille = [[random.choice([0, 1]) for _ in range(LARGEUR_GRILLE)] for _ in range(HAUTEUR_GRILLE)]

    def dessiner_grille():
        toile.delete("all")
        for y in range(HAUTEUR_GRILLE):
            for x in range(LARGEUR_GRILLE):
                if grille[y][x] == 1:
                    toile.create_rectangle(
                        x * TAILLE_CELLULE, y * TAILLE_CELLULE,
                        (x + 1) * TAILLE_CELLULE, (y + 1) * TAILLE_CELLULE,
                        fill="black"
                    )

    def mettre_a_jour_grille():
        nouvelle_grille = [[0 for _ in range(LARGEUR_GRILLE)] for _ in range(HAUTEUR_GRILLE)]
        for y in range(HAUTEUR_GRILLE):
            for x in range(LARGEUR_GRILLE):
                voisins_vivants = sum(
                    grille[(y + dy) % HAUTEUR_GRILLE][(x + dx) % LARGEUR_GRILLE]
                    for dx in [-1, 0, 1] for dy in [-1, 0, 1]
                    if (dx, dy) != (0, 0)
                )
                if grille[y][x] == 1 and voisins_vivants in [2, 3]:
                    nouvelle_grille[y][x] = 1
                elif grille[y][x] == 0 and voisins_vivants == 3:
                    nouvelle_grille[y][x] = 1
        return nouvelle_grille

    def boucle_jeu():
        nonlocal grille
        grille = mettre_a_jour_grille()
        dessiner_grille()
        racine.after(100, boucle_jeu)

    dessiner_grille()
    racine.after(100, boucle_jeu)
    racine.mainloop()