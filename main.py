from restritions import *
from conversor import *
from genetic_algo import *


instance = generate_population(21, 10, 21)

print(genetic1(instance, 10, 0, 1, 100, 25, 10, 21))

