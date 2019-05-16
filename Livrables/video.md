# Vidéo présentation du projet

## Scénario

1. On parle de l'optmisation en générale
    1. Définition
    2. Problèmes à résoudre par optimisation
        1. Taille fichier
        2. Temps exécution
    3. Outils qui existent
2. On se concentre sur flow graph = 1er outil
    1. Définition
    2. Utilité
        1. Visuel humain
        2. Optimisation machine
    3. Présentation de nos outils
3. On se concentre sur dead code detection = 2ème outil
    1. Définition
    2. Utilité
        1. Optimisation machine
    3. Présentation de notre outil
        1. Aide au programmeur
4. Conclusion
    1. Cas extrême optimisation marrant pour percuter les gens

On utilise un dévelopeur personnage comme fil rouge

## Script

(1) Qu'est-ce que l'optimisation de code ? 

> point d'interrogation qui pop
   (1.1) En programmation informatique, l'optimisation de code est la pratique consistant à augmenter l'efficacité du code d'un programme ou d'une librairie logicielle, ainsi que les différentes techniques permettant d'y parvenir.
   
> écran séparé en deux
   (1.2) Nous nous sommes concentrés lors de ce projet sur deux types d'optimisation :

        (1.2.1) réduire la place prise en mémoire par le code ayant été écrit,

        (1.2.2) et améliorer la rapidité d'exécution du programme.

    (1.3) De très nombreux outils plus ou moins connus sont dédiés à l'optimisation de code, et ce dans tous les languages de programmation. La bibliothèque de compilation gcc, par exemple, permet à l'utilisateur d'appliquer facilement nombre d'optimisations à son code.


(2) Dans le cadre de notre projet, nous avons tout d'abord tenté d'utiliser les informations apportées par le Control Flow Graph d'un code afin de l'optimiser.

> image de CFG
    (2.1) Un Control Flow Graph, ou Graphe de flot de contrôle en français, est la représentation sous forme de graphe de tous les chemins que peut suivre un programme pendant son exécution.

> personnage devant un tableau dans une réunion
    (2.2) Cela peut être utilisé pour améliorer le code, tout comme pour le représenter de manière plus claire à un interlocuteur.

> avant-après notre opti
    (2.3) Nous avons ainsi développé une extension d'une bibliothèque permettant d'extraire un Control Flot Graph d'un code, afin de rendre la représentation celui-ci plus clair en encore. Les appels à fonction sont maintenant plus visibles, représentés par des flêches de couleur.


(3) Nous nous sommes ensuite éloigné des Control Flow Graph, et tenté d'apporter de l'optimisation de code en détectant du code mort !

    (3.1) La détection de code mort, ou dead code detection, consiste à détecter automatiquement des parties du code qui ne sont jamais executées, et de les supprimer.

> visage un peu content, puis visage très content
    (3.2) Supprimer des pans entier de code permet non seulement de réduire la place mémoire du code, mais peut même dans certains cas faire grandement gagner le programme en vitesse d'exécution ! En effet, si des conditions s'avèrent toujours vraies ou fausses, il est possible de les supprimer et d'exécuter ou non le code sous-jacent. Le programme n'aura donc plus à tester ces conditions ce qui représente un gain de temps et une économie d'énergie.

- Tu n'as pas parlé de l'optimisation avant qu'on a fait:
  
>
    (3.3) L'optimisation dont nous avons montré la possibilité d'implémentation permet d'aider le programmeur à voir les zones de code mort, dans le cas où des conditions sont toujours vérifiées, ou au contraire ne le sont jamais.

> image de code avec la boucle, puis gros marquage rouge sur la boucle while pour la barrer
(4) Cette optimisation permet dans certains cas de gagner un très grand temps d'exécution ! Ici, la fonction appelée dans la boucle while ne peut jamais s'exécuter, puisque la condition pour son exécution n'est jamais vérifiée. Il serait donc possible de supprimer toute la boucle, enlevant un important temps de calcul.
