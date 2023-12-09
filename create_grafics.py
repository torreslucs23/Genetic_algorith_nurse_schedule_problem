import pandas as pd
from genetic_algo import *


import matplotlib.pyplot as plt
import numpy as np

# Assume that the genetic function returns numpy arrays
# Make sure to replace this with your own data
print("Please type the file name, otherwise it will be "\
        "used 'test.txt' as the default file name.")

file_name = input("")

if(file_name == ""):
    file_name = "test.txt"

try:
    file = open(file_name, "r")

    first_line = file.readline().split()
    second_line = file.readline().split()

    file.close()

except Exception as exc:
    raise OSError("Something went wrong while reading" \
                    "the file!") from exc

n_individual, k, n = [int(i) for i in first_line]
instance = generate_population(n_individual, k, n)

n_mutation, t_crossover,  t_mutation, n_iterations, n_elitism = [int(i) for i in second_line]
mean_f, min_f, max_f = (genetic(instance, n_mutation, t_crossover,  t_mutation, n_iterations, n_elitism, k, n))

# Generate an array of indices for the x-axis
indices = np.arange(len(mean_f))

# Create a line plot
plt.plot(indices, mean_f, color='blue', label='Mean Fit')
plt.plot(indices, min_f, color='green', label='Min Fit')
plt.plot(indices, max_f, color='red', label='Max Fit')

# Add labels and title to the plot
plt.xlabel('Iteration')
plt.ylabel('Fitness Values')
plt.title('Fitness Plot (Minimum, Maximum, Mean)')

# Add a legend
plt.legend()

# Display the plot
plt.show()


