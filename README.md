# US States Game

Ce projet utilise Python avec les modules Turtle et Pandas pour créer un jeu interactif de reconnaissance des États des États-Unis.

## Présentation du Projet

Le jeu affiche une carte des États des États-Unis et demande à l'utilisateur de deviner les noms des différents États. Si l'utilisateur devine correctement un État, celui-ci est placé sur la carte. Les données des États sont stockées dans un fichier CSV ("50_states.csv") et sont traitées à l'aide du module Pandas pour la gestion des données.

## Contenu du Projet

### Fichiers inclus :

- `main.py`: Le fichier principal du jeu, qui gère l'interface utilisateur et la logique du jeu en utilisant les modules Turtle et Pandas.
- `50_states.csv`: Un fichier CSV contenant une liste des États des États-Unis à deviner, utilisé pour charger les données dans le jeu.

### Installation et Configuration :

- Pyhton 3.9.6
- importation du module pandas

#List Comprehension #pandas

## Comment Jouer ?

Exécutez le fichier `main.py` pour démarrer le jeu.

- La carte des États des États-Unis s'affichera à l'écran.
- Saisissez le nom d'un État lorsque vous êtes invité.
- Si vous devinez correctement, le nom de l'État apparaîtra sur la carte.
- Pour quitter le jeu, saisissez "Exit". Une liste des États manquants sera alors sauvegardée dans un fichier "states_to_learn.csv".

## Apperçu de l'interface
![Game Screenshot](/assets/interface.png)

### Remarques
- Projet réalisé dans le cadre du cours [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) de Angela Yu sur la plateforme Udemy.
