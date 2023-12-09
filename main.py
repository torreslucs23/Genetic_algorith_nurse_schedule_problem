from restritions import *
from conversor import *
from genetic_algo import *


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
res = (genetic(instance, n_mutation, t_crossover,  t_mutation, n_iterations, n_elitism, k, n))
