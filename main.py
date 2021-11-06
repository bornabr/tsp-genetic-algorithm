import tsplib95

from utils import initial_population
from utils import generate_genration


def TSP_GA(filename, n_generations, population_size, tournament_size, parents_size, mutation_rate, elite_size):
	problem = tsplib95.load('./problems/' + filename)
	
	population = initial_population(problem, population_size)
	
	for i in range(n_generations):
		population = generate_genration(
			i, population, tournament_size, parents_size, mutation_rate, elite_size)
	
	print([x.distance for x in population])
	
	print('Best Answer:')
	print(population[0].permutation, population[0].distance)

def bayg29():
	population_size = 100

	tournament_size = 90

	parents_size = 40

	elite_size = 20

	mutation_rate = 0.01

	n_generations = 100

	TSP_GA('bayg29.tsp', n_generations, population_size, tournament_size,
	       parents_size, mutation_rate, elite_size)


def bayg29():
	population_size = 100

	tournament_size = 90

	parents_size = 40

	elite_size = 20

	mutation_rate = 0.01

	n_generations = 100

	TSP_GA('bayg29.tsp', n_generations, population_size, tournament_size,
	       parents_size, mutation_rate, elite_size)


def gr229():
	population_size = 100

	tournament_size = 90

	parents_size = 70

	elite_size = 30

	mutation_rate = 0.05

	n_generations = 100

	TSP_GA('gr229.tsp', n_generations, population_size, tournament_size,
	       parents_size, mutation_rate, elite_size)


def pr1002():
	population_size = 100

	tournament_size = 90

	parents_size = 50

	elite_size = 35

	mutation_rate = 0.05

	n_generations = 150

	TSP_GA('pr1002.tsp', n_generations, population_size, tournament_size,
	       parents_size, mutation_rate, elite_size)

# bayg29()

gr229()

# pr1002()
