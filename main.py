from restritions import *
from conversor import *
from genetic_algo import *



instance = generate_population(21, 10, 21)

res = (genetic(instance, 50, 0, 0, 100, 25, 10, 21))

