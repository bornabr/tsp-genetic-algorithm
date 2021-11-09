# TSP Problem with Genetic Algorithm
## Data
The input of this problem files with `tsp` format. I used the `tsplib95` library for weighted test cases (`bayg29`) and a self-written loader for test cases with coordinations.

## Algorithm
At first, we generate our initial population with random routes(permutations).

The main process is a loop with several sections. At the end of every iteration in this loop, a new generation is born, preferably with better individuals.

Here is each section of this process:

### Selection
The first thing we do with the previous generation is to select a subset of them as our parents. The primary consideration here is to make a balance between elites and vulgar to prevent overfitting or underfitting.

The algorithm used for this matter is tournament selection. For this, we choose a subset of the population by random, then we sort them based on their fitness and select a number of them as parents.

### Breeding
With the parents being chosen, it is time for mating them with each other. Two individuals create a child with ordered recombination.

For choosing each pair, we shuffle parents and mate them by random. We repeat this shuffling until the number of our children has reached the population size.

### Mutation
We have a parameter called the `mutation_rate`, which specifies the probability of mutation.

The mutations in this problem are done by swapping two cities(genes) in a permutation.

### Replacement
The final step in the loop is to specify the next generation. We have considered a mix of children and parents because we want to keep the best parents for the next generation.
We replace a fixed number of worst children with the best parents.

## Test
### bayg29
My best distances were between 1600 to 1800 and here is one of them:
```
Epoch 0 :       Population total fitness: 0.021402390435083837  Best fitness: 0.000275178866263071      Least Distance: 3634
Epoch 1 :       Population total fitness: 0.022400741669908814  Best fitness: 0.00028694404591104734    Least Distance: 3485
Epoch 2 :       Population total fitness: 0.02321754970711249   Best fitness: 0.000299311583358276      Least Distance: 3341
Epoch 3 :       Population total fitness: 0.024596784139334586  Best fitness: 0.00030321406913280777    Least Distance: 3298
Epoch 4 :       Population total fitness: 0.025508500567304724  Best fitness: 0.00031655587211142766    Least Distance: 3159
Epoch 5 :       Population total fitness: 0.02567080676446863   Best fitness: 0.00031655587211142766    Least Distance: 3159
Epoch 6 :       Population total fitness: 0.026095669980930384  Best fitness: 0.00031826861871419476    Least Distance: 3142
Epoch 7 :       Population total fitness: 0.026213325051129905  Best fitness: 0.0003176620076238882     Least Distance: 3148
...
Epoch 92 :      Population total fitness: 0.046347892289803405  Best fitness: 0.0005633802816901409     Least Distance: 1775
Epoch 93 :      Population total fitness: 0.04640791685328948   Best fitness: 0.0005633802816901409     Least Distance: 1775
Epoch 94 :      Population total fitness: 0.0463885029225474    Best fitness: 0.000572737686139748      Least Distance: 1746
Epoch 95 :      Population total fitness: 0.04655714750065836   Best fitness: 0.000572737686139748      Least Distance: 1746
Epoch 96 :      Population total fitness: 0.04607831403892826   Best fitness: 0.000572737686139748      Least Distance: 1746
Epoch 97 :      Population total fitness: 0.04588737374610269   Best fitness: 0.000572737686139748      Least Distance: 1746
Epoch 98 :      Population total fitness: 0.04635046560907124   Best fitness: 0.000572737686139748      Least Distance: 1746
Epoch 99 :      Population total fitness: 0.0466206756566057    Best fitness: 0.000572737686139748      Least Distance: 1746
Best Answer:
[13, 4, 20, 10, 2, 29, 3, 26, 6, 12, 9, 5, 21, 28, 1, 24, 8, 23, 27, 16, 7, 25, 19, 15, 18, 17, 14, 11, 22] 1746
```


## Considerations
- Because we want to optimize our answers based on the total distance of the cycle, our fitness function is `1/total_distance` (so we try to maximize fitness).

