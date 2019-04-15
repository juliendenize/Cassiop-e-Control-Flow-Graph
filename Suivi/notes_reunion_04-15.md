- ASQ -> arbre de représentation du code
- table de symbole

- constant propagation
- abstract interpretation -> simulation des valeurs que peuvent avoir une variable (variable analysis) OU dataflow analysis

- vérifier avec -O3 (et voir si ça ne fait pas l'opti après la génération de graphe)

- détection de mutants équivalents via trivial compiler detection

- possibilité d'optimiser les condtions et boucles -> problème: boucles infinies parfois désirables

- pour voir si une condition est toujours vraie ou toujours fausse : SAT, FPO, check-sat, rise4fun.com/z3

- pas d'intérêt à l'implémenter sur pydot

- générer en assembleur (peut-être gcc -S) avec gcc le code avec ou sans l'optimisation -O3 afin de comparer ensuite les deux résultats

- mots clés sur lesquels se continuer de se concentrer : dead code elimination
