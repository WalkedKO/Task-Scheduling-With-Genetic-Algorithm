from schedule import Schedule
from numpy.random import choice, randint
"""
The whole process of genetic algorithm.
"""
class Specie:
    def __init__(self, workers_set, products_set, time_units, population, max_gen, number_to_select):
        """
        :param workers_set: list of workers
        :param products_set: list of products
        :param time_units: units of time
        :param population: maximum population in a generation
        :param max_gen: maximum number of generations
        :param number_to_select: number of individuals selected to reproduction at each generation
        """
        self.workers_set = workers_set
        self.products_set = products_set
        self.time_units = time_units
        self.population = population
        self.max_gen = max_gen
        self.best_of_generations = []
        self.select_nr = number_to_select
    def fps_selection(self, generation):
        """
        Selects which individuals will going to reproduce and create a new generation
        :param generation: list of all generation's individuals
        :return: list of individuals to reproduce
        """
        fit_sum = sum(fit for i, fit in generation)
        population = [i for i, fit in generation]
        fitness = [fit / fit_sum for i, fit in generation]
        return population[choice(len(population),  p=fitness)]
    def first_gen(self):
        """
        generates the first generation
        :return: list of individuals, first generation
        """
        gen = [Schedule(self.workers_set, self.products_set, self.time_units) for i in range(self.population)]
        for i in gen:
            i.randomize(self.time_units ** 2)
        return gen
    def find_best(self):
        """
        Finds list of all the best individuals from each generation. Runs the whole procedure by the way
        :return: list of the best individuals from each generation. Elements are tuples. 0th index is the individual and 1th is their fitness score
        """
        # create first gen
        current_gen = self.first_gen()
        for i in range(self.max_gen):
            print("Gen: ", i)
            gen_pairs = [(i, i.evaluate_fitness()) for i in current_gen]
            to_crossover = [self.fps_selection(gen_pairs) for i in range(self.select_nr)]
            current_gen.clear()
            while len(current_gen) < self.population:
                new_individual = Schedule(self.workers_set, self.products_set, self.time_units)
                father = to_crossover[randint(0, self.select_nr)]
                mother = to_crossover[randint(0, self.select_nr)]
                new_individual.crossover(father, mother)
                current_gen.append(new_individual)
            self.best_of_generations.append(max(gen_pairs, key=lambda x: x[1]))
        return self.best_of_generations.copy()
