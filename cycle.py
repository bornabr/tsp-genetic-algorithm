class Cycle:
	def __init__(self, problem, permutation):
		if not Cycle.is_cycle(problem, permutation):
			raise("Not a cycle")

		self.problem = problem
		self.permutation = permutation
		
		self.distance = None
		self.get_distance()
		
		self.fitness = None
		self.get_fitness()
		
		
	
	@staticmethod
	def is_cycle(problem, permutation):
		tmp = set(permutation)
		if len(tmp) != len(permutation):
			return False
		
		# for i in range(1, len(permutation)):
		# 	if not (permutation[i-1], permutation[i]) in list(problem.get_edges()):
		# 		return False
		
		return True
	
	def get_distance(self):
		if self.distance is not None:
			return self.distance
		self.distance = 0
		for i in range(1, len(self.permutation)):
			self.distance += self.problem.get_weight(
				self.permutation[i-1], self.permutation[i])
		
		return self.distance

	def get_fitness(self):
		if self.fitness is not None:
			return self.fitness
		self.fitness = 1/float(self.distance)
		return self.fitness
