# 14/02/2019

## Récapitulatif

### Tests
Plusieurs répertoire dans Tests/ ont été créés pour comprendre comment se génèrent les graphes.

### Intuitions
On a pu voir qu'il est possible de travailler sur les fichiers dot pour créer nous-même des transitions.
On aimerait bien trouver les docs nous permettant de pouvoir soit changer le code source (solution la moins pratique) soit pouvoir travailler avec un script qu'on écrit sur les cfg et dot pour faire ce qu'on veut.

![Image of Yaktocat](../Tests/test_fleche_fonction/graphe.png)

On aimerait pouvoir relier les fonctions entre elles, et donc pour ça on doit pouvoir créer des nouveaux noeuds qui appellent ces fonctions et un autre qui récupère le résultat(s'il y en a un).

### Plusieurs appels imbriqués de fonction
On a voulu tester ce que ça faisait si on appelait une fonction en lui donnant en paramètre le retour d'une autre fonction pour voir si dans le cfg c'était géré comme des appels successifs, ce qui est bien le cas. Ce qui nous facilite la vie.

### Calculs avec parenthèses
On a aussi testé des calculs avec des parenthèses pour voir si il faisait une opération à la fois dans le cfg ou s'il faisait tout d'un coup. Il fait bien une opération à la fois ce qui nous facilite également la vie.

![Image of Yaktocat](../Tests/test_calculs_avec_parentheses/graphe.png)

### Ajout de flèches entre fonctions à la main
On a réussi à créer un nouveau node s'arrêtant à un appel de fonction pour le relier au graphe de la fonction appelée.

![Image of Yaktocat](../Tests/test_creation_nodes/graphe.png)

## Trucs à faire
- [x] réussir à prendre les fonctions qu'on a créé pour relier les fonctions
- [x] trouver la doc gcc vers dot

# 18/02/2019

## Récapitulatif

### Tests/Try_modelisation

Nous avons modélisé la manière dont nous voulons gérer les fonctions dans le graphe. Nous avons décidé de créer une instruction `call fonction(args)` pour appeler une fonction à partir d'un noeud qui va être relié au noeud entry de cette fonction.

Ensuite la valeur de retour est stockée dans la variable qui était prévu à cet effet comme ceci `_1 = return fonction(args)`.

Voici le résultat:
![Image of Yaktocat](../Tests/Try_modelisation/graph.png)

# 21/02/2019

## Récapitulatif

### Test pydot

On voulait trouver un parser de fichiers dot. On a trouvé la bibliothèque python pydot qui permet d'importer un fichier dot afin de créer une structure de graphe définie par cette bibliothèque afin de travailler sur les objets plutôt que le fichier dot.

Dans le dossier `/Notebooks` on a créé un premier notebook testant cette librairie et on a pu voir qu'il est possible de changer la structure du graphe comme on pouvait le faire à la main pour créer de nouveaux nodes et edges.

Maintenant nous allons devoir parser les labels des nodes pour trouver où sont les fonctions et créer des noeuds et edges en fonction de ce qu'on a trouvé.

### Création du script

On a commencé à créer le script python pour faire des liens entre les fonctions, c'est le deuxième notebook. On continuera le 25/02/2019.

# 25/02/2019

## Récapitualtif
On a continué le script python en faisant beaucoup de regex pour parser les labels, on poursuit le 28/02 ou 01/03.

# 28/02/2019

## Récapitulatif
On a encore continué le script, on a presque fini de créer le nouveau noeud, ensuite il faudra faire les edges quand on aura terminé.

# 3/03/2019

## Récapitulatif

On a fini le script et testé sur différents cas. On merge la branch script et master afin de marquer le coup.

# 11/03/2019

## Récapitualtif
On a cherché comment utiliser networkx pour analyser les graphes: cycle, betweeness, ...

On n'a pas trouvé et décidé de chercher chacun de son côté comment le faire.

# 18/03/2019

## Récapitulatif
On a réussi à construire un graphe networkx à partir d'un graph pydot.

On a aussi extrait deux informations du graphe: les degrés entrants pour chaque noeud ainsi que la betweeness de chaque noeud.

On a évoqué l'idée qu'il faudrait peut-être analyser chaque fonction dans le fichier généré de base par GCC ainsi que le fichier modifié pour pouvoir analyser le programme dans son ensemble ainsi que pour chaque fonction.

## Todo

- [x] Trouver des informations à tirer du graph transformé par notre premier script.
- [x] Implémenter ces idées.
- [x] Noter les idées qui seraient spécifiques à des fonctions.

# 1/04/2019

## Récapitulatif
On a pu constater que l'analyse de graphe ne menait pas à grand chose si on regarde les propriétés basiques. On va juste regarder si le graphe est complet en plus de ce qui a été fait.

Certaines petites propriétés plus liées au code peuvent être intéressantes à chercher: partial dead code, conditions imbriquées inutiles.


## Todo
- [x] Voir si graphe complet
- [x] Recherche partial dead code
- [] Etudier fonctionnement compilateur (étapes)

## Roadmap
- Une semaine de recherches
- Lundi 8: mise en commun de 14h à 16h-18h
- Jeudi 11: développement

# 11/04/2019

## Récapitulatif
Le compilateur travaille automatiquement sur les conditions true sans variables
et supprime les conditions vides.
On va se pencher plus sur le côté compilateur. Voir si on décide de se pencher vers la compilation ou parser.

# 18/04/2019

## Récapitulatif

Voilà ce qu'on a trouvé que gcc n'optimise pas:

~~~
while(b < a) {
    if (b < a + 10) {
        return 11;
    }
    return 10;
}
~~~
~~~
if (b > 0)
{
    if(b < 100)
    {
        if (b % 11 == 0)
        {
                return 11;
        }
    }
}
~~~

On pense que GCC fait une analyse statique des valeurs qu'ils remplacent quand il le peut ce qui explique l'optimisation des conditions en générales car les valeurs, ou plages valeurs sont directement remplacées. Cependant quand on lui fournit des valeurs qu'il ne peut remplacer on voit très vite du code non optimisé, et donc du code mort qui pourrait être supprimé.

## Roadmap

Point jeudi 25 à effectuer et d'ici là recherches sûr si ce qu'on a trouvé existe et preuves formelles.

# 25/04/2019

## Récapitulatif

On a trouvé des articles permettant de tester les conditions d'un programme et détecter des bugs et deadcode. On peut s'en inspirer pour la notation et la méthode et on pense que ce n'est pas exactement ce qu'on fait donc on continue sur notre idée.

## Todo durant les vacances

- [x] planning
- [x] compréhension des articles inconsitencies
- [] lecture du cours compilateur
- [] commencer le POC

## Roadmap
Point jeudi 2 mai pour suivre notre avancée et faire une mise en commun.
Point le dimanche 5 mai pour finaliser avant le rendeez-vous avec Jorge.


<<<<<<< HEAD
# 5/05/2019

## Récapitulatif

On a effectué le planning à rendre pour le 6 mai.

On a mis en commun nos réflexions en parlant de recherches sur l'optimisation, deadcode detection, ... On attend le 6 mai pour discuter avec Jorge de la suite.
=======

# 06/05/2019

## Notes

AST: Abstract Syntax Tree (plus approprié que le CFG pour décrire la structure du programme)

## Récapitulatif

On a précisé avec Jorge les attentes concernant le POC.
On a pu voir que l'outil de l'article inconsistencies était introuvable.
On va utiliser le parser pycparser pour parser l'ast d'un programme simple afin de l'optimiser.

## Todo

- [] comparer détection erreur avec les deux autres outils mentionnés dans l'article inconsistencies
- [] script détection et correction d'erreur
>>>>>>> 83a32ffda9fa9a656155a62cb3b348279d05054f
