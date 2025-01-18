# Jeu de la Vie

Le Jeu de la Vie est un automate cellulaire, un modèle mathématique qui simule l'évolution d'une grille bidimensionnelle de cellules au fil du temps. Ce projet est une implémentation simple du Jeu de la Vie utilisant Python et la bibliothèque Tkinter pour l'interface graphique.

## Installation

Pour exécuter le Jeu de la Vie, vous devez avoir Python 3 installé sur votre système. Vous pouvez télécharger Python depuis le site officiel : [https://www.python.org/downloads/](https://www.python.org/downloads/)

Une fois Python installé, vous pouvez cloner le dépôt et lancer le jeu :

```
git clone https://github.com/bob900-cod/jeu-de-la-vie.git
cd jeu-de-la-vie
python main.py
```
## Utilisation

Lorsque vous exécutez le fichier `main.py`, une fenêtre s'ouvrira affichant une grille de cellules. L'état initial de la grille est généré aléatoirement, avec certaines cellules vivantes (noires) et d'autres mortes (blanches).

Le jeu commence alors, avec les cellules évoluant selon les règles du Jeu de la Vie :

- Toute cellule vivante ayant moins de deux voisins vivants meurt, comme si elle était victime de sous-population.
- Toute cellule vivante ayant deux ou trois voisins vivants survit à la génération suivante.
- Toute cellule vivante ayant plus de trois voisins vivants meurt, comme si elle était victime de surpopulation.
- Toute cellule morte ayant exactement trois voisins vivants devient une cellule vivante, comme par reproduction.

Le jeu continue indéfiniment, avec la grille qui se met à jour toutes les 100 millisecondes.

## Fonctionnement

La fonctionnalité principale du Jeu de la Vie est implémentée dans le fichier `window.py`, qui contient les fonctions suivantes :

- `creer_fenetre()`: Crée la fenêtre principale et le canevas où le jeu est affiché.
- `dessiner_grille()`: Dessine l'état actuel de la grille sur le canevas.
- `mettre_a_jour_grille()`: Calcule l'état suivant de la grille en fonction de l'état actuel et des règles du Jeu de la Vie.
- `boucle_jeu()`: Exécute la boucle du jeu, met à jour la grille et redessine le canevas.

Le fichier `main.py` est le point d'entrée de l'application, qui appelle simplement la fonction `creer_fenetre()` pour démarrer le jeu.
