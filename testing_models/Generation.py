import numpy as np
from Individual import Individual


class Generation:
    def __init__(self, has_weighted_reproduction, has_uniform_crossover, has_pair_reproduction, has_selection, population=[]):

        self.seed = 19680801
        np.random.seed(self.seed)

        self.has_weighted_reproduction  = has_weighted_reproduction
        self.has_uniform_crossover      = has_uniform_crossover
        self.has_pair_reproduction      = has_pair_reproduction
        self.has_selection              = has_selection

        self.mutation_rate              = 0.1
        self.selction_rate              = 0.1
        self.shifts_per_day             = 3
        self.number_of_days             = 7
        self.total_shifts               = self.shifts_per_day * self.number_of_days


        self.population_size            = 100
        self.population                 = population

        if(len(population) == 0):
            self.use_random_population()


    def use_random_population(self):

        missing_population = self.population_size - self.population

        for i in range(missing_population):

            genetic_code     = np.random.randint(2, size=self.total_shifts)
            individual       = Individual(genetic_code)

            self.population += [individual]


    def get_fit_data(self):

        fittest = max(self.population)
        avg_fit = np.mean(self.population)
        
        return (fittest, avg_fit)


    def get_next(self):

        next_population = []

        if(self.has_pair_reproduction):
            next_population = self.pair_reproduction()

            if(self.has_selection):
                next_population += self.selection()
        
        else:
            if(self.has_weighted_reproduction):
                next_population += self.random_weighted_reproduction()
            else:
                next_population  = self.random_reproduction()
