import matplolib.pyplot as plt
import numpy as np
from handler import *
from parameters import *


test_cases_parameters   = build_tests_parameter()
total_test_cases        = len(test_cases_parameters)

samples_by_parameters   = np.array([[] for i in range(total_test_cases)])
number_of_iterations    = 1

for i in range(number_of_iterations):
    count = 0
    for paramenters in test_cases_parameters:

        first_fittest, last_fittest      = run_selection(parameters)
        samples_by_paramenters[count]   += [(first_filttest, last_fittest)]

        count += 1


np.random.seed(19680801) # Fixing the randomness

colors              = np.random.rand(total_test_cases)
samples_and_colors  = zip(samples_by_parameters, colors)

indexes             = [i for i in range(number_of_iterations)]

for samples, color in samples_and_colors:

    init_fitnesses  = [sample[0] for sample in samples]
    plt.scatter(init_fitnesses, indexes, c=color, alpha=0.6)

    final_fitnesses = np.array([sample[1] for sample in samples])
    plt.scatter(final_fitnesses, indexes, c=color, alpha=0.6)

plt.show()
