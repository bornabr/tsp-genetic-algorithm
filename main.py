from loader import Problem
from utils import TSP_GA

def bayg29():
	population_size = 100

	tournament_size = 80

	parents_size = 10

	elite_size = 5

	mutation_rate = 0.01

	n_generations = 1000

	TSP_GA('bayg29.tsp', n_generations, population_size, tournament_size,
	       parents_size, mutation_rate, elite_size)


def gr229():
	population_size = 200

	tournament_size = 160

	parents_size = 10

	elite_size = 5

	mutation_rate = 0.005

	n_generations = 10000

	problem = Problem('./problems/gr229.tsp')

	TSP_GA('gr229.tsp', n_generations, population_size, tournament_size,
	       parents_size, mutation_rate, elite_size, problem)


def pr1002():
	population_size = 200

	tournament_size = 140

	parents_size = 10

	elite_size = 5

	mutation_rate = 0.001

	n_generations = 1000

	problem = Problem('./problems/pr1002.tsp')

	TSP_GA('pr1002.tsp', n_generations, population_size, tournament_size,
	       parents_size, mutation_rate, elite_size, problem)

# bayg29()

gr229()

# pr1002()
