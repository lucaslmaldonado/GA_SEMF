from semf import SEMF
from math import inf

class GA:

    def __init__(self, n):
        self.size = n
        self.population = []
        for _1 in range(self.size):
            self.population.append(SEMF())

    def calc_fitness(self, data):
        for i in range(self.size):
            self.population[i].calc_fitness(data)

    def mate(self):
        self.population = sorted(self.population, key=lambda x:x.fitness)
        parent1 = self.population[-1]
        parent2 = self.population[-2]
        for i in range(self.size):
            self.population[i] = SEMF(parent1, parent2)

    def mutate(self, mu, epsilon):
        for i in range(self.size):
            self.population[i].mutate(mu, epsilon)

    def find_best(self):
        max_fitness = -inf
        max_fitness_id = 0
        for i in range(self.size):
            if self.population[i].fitness > max_fitness:
                max_fitness = self.population[i].fitness
                max_fitness_id = i
        max_fitness_str = "Max fitness: {}\n".format(max_fitness)
        return max_fitness_str, self.population[max_fitness_id].get_self()    