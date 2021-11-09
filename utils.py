import random
import tsplib95

from cycle import Cycle

def chromosome_generator(size):
	return random.sample(range(1, size+1), size)


def initial_population(problem, population_size):
	return [Cycle(problem, chromosome_generator(problem.dimension))
		 for _ in range(population_size)]


def tournament_selection(population, tournament_size, parents_size):
	parents = random.choices(population, k=tournament_size)
	parents = sorted(parents, key=lambda agent: agent.fitness, reverse=True)
	return parents[:parents_size]


def breed(parent1, parent2):
	child = []
	childP1 = []
	childP2 = []

	geneA = int(random.random() * len(parent1.permutation))
	geneB = int(random.random() * len(parent1.permutation))

	start = min(geneA, geneB)
	end = max(geneA, geneB)

	childP1 = parent1.permutation[start:end]

	childP2 = [item for item in parent2.permutation if item not in childP1]

	child = Cycle(parent1.problem, childP1 + childP2)
	
	return child


def breed_population(parents, population_size):
	children = []
	
	rate = int((population_size/len(parents))*2)
	
	for _ in range(rate):
		random.shuffle(parents)
		for i in range(int(len(parents)/2)):
			child = breed(parents[i], parents[len(parents)-i-1])
			children.append(child)
	
	return children

def mutate(individual, mutation_rate):
	permutation = individual.permutation
	for swapped in range(len(permutation)):
		if(random.random() < mutation_rate):
			swapWith = int(random.random() * len(permutation))

			city1 = permutation[swapped]
			city2 = permutation[swapWith]

			permutation[swapped] = city2
			permutation[swapWith] = city1
	mutated = Cycle(individual.problem, permutation)
	return mutated


def mutate_population(population, mutation_rate):
	mutated_children = []

	for ind in range(0, len(population)):
		mutatedInd = mutate(population[ind], mutation_rate)
		mutated_children.append(mutatedInd)
	
	return mutated_children


def replacement(mutated_children, parents, elite_size):
	mutated_children = sorted(
		mutated_children, key=lambda agent: agent.fitness, reverse=True)
	parents = sorted(parents, key=lambda agent: agent.fitness, reverse=True)
	
	mutated_children = mutated_children[:-elite_size] + parents[:elite_size]
	
	mutated_children = sorted(
		mutated_children, key=lambda agent: agent.fitness, reverse=True)
	
	return mutated_children

def evaluate(population):
	pop_fitness = [agent.fitness for agent in population]
	pop_distance = [agent.distance for agent in population]
	
	return sum(pop_fitness), max(pop_fitness), min(pop_distance)


def generate_genration(epoch, previous_population, tournament_size, parents_size, mutation_rate, elite_size):
	parents = tournament_selection(
		previous_population, tournament_size, parents_size)
	
	children = breed_population(parents, len(previous_population))
	
	mutated_children = mutate_population(children, mutation_rate)
	
	next_population = replacement(mutated_children, parents, elite_size)
	
	eval_ = evaluate(next_population)
	
	print("Epoch", epoch, ":\tPopulation total fitness:",
	      eval_[0], "\tBest fitness:", eval_[1], "\tLeast Distance:", eval_[2])
	
	return next_population


def TSP_GA(filename, n_generations, population_size, tournament_size, parents_size, mutation_rate, elite_size, problem=None):
	if problem is None:
		problem = tsplib95.load('./problems/' + filename)

	population = initial_population(problem, population_size)

	for i in range(n_generations):
		population = generate_genration(
			i, population, tournament_size, parents_size, mutation_rate, elite_size)

	print('Best Answer:')
	print(population[0].permutation, population[0].distance)
