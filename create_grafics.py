import pandas as pd
from genetic_algo import *


import matplotlib.pyplot as plt
import numpy as np

# Assume that the genetic function returns numpy arrays
# Make sure to replace this with your own data
instance = generate_population(1000, 10, 21)
mean_f, min_f, max_f = genetic(instance, 10, 1, 1, 1000, 10, 10, 21)

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


