# 18/02/2019

## Récapitulatif

### Tests/Try_modelisation

Nous avons modélisé la manière dont nous voulons gérer les fonctions dans le graphe. Nous avons décidé de créer une instruction `call fonction(args)` pour appeler une fonction à partir d'un noeud qui va être relié au noeud entry de cette fonction.

Ensuite la valeur de retour est stockée dans la variable qui était prévu à cet effet comme ceci `_1 = return fonction(args)`.

Voici le résultat:
![Image of Yaktocat](../Tests/Try_modelisation/graph.png)