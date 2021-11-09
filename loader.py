class Problem:
	def __init__(self, filepath):
		f = open(filepath, 'r')
		lines = f.readlines()
		self.coordinations = []
		start = False
		for line in lines:
			if start:
				line = line.strip().split()
				if len(line) < 3:
					break
				self.coordinations.append((float(line[1]), float(line[2])))
				continue
			
			if 'DIMENSION' in line:
				line = line.split(':')
				self.dimension = int(line[1].strip())
				continue
			
			if 'NODE_COORD_SECTION' in line:
				start = True
		self.calculate_weights()
	
	def calculate_weights(self):
		self.weights = []
		for first_coordination in self.coordinations:
			weights = []
			for second_coordination in self.coordinations:
				weights.append((((first_coordination[0]-second_coordination[0])**2) +
				        ((first_coordination[1]-second_coordination[1])**2))**0.5)
			self.weights.append(weights)
	
	def get_weight(self, start, end):
		return self.weights[start-1][end-1]
