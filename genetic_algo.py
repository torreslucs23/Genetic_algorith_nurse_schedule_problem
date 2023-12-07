from restritions import *
from conversor import *
from random import randint, shuffle

#this function generate all individuals of a population
#k = nurses n = shifts
def generate_population(n_individual,k, n):
    population = []
    for i in range(n_individual):
        individual = []
        for w in range(k):
            for j in range(n):
                num = randint(0,1)
                individual.append(str(num))
        population.append(''.join(individual))
    print(population)
    return population
        

#Function that mutates a chromosome according to the probability rate.
def mutation0(n_mutation, chromosome):
    n = randint(0,100)
    if n > n_mutation:
        return chromosome
    
    chrom = [i for i in chromosome]
    index = randint(0, len(chromosome) - 1)
    if chrom[index] == '0':
        chrom[index] = '1'

    else:
        chrom[index] = '0'

    return ''.join(chrom)

#Function that selects a random individual from the population and performs mutation
#note that rate is rounded to its integer value
def mutation1(n_mutation, population):
    l_popu = len(population)
    l = [i for i in range(l_popu)]
    shuffle(l)
    n_chroms = int(n_mutation*l_popu/100)
    for i in range(n_chroms):
        new_chrom = [w for w in population[l[i]]]
        n = randint(0,len(population[l[i]]) - 1)
        if new_chrom[n] == '0':
            new_chrom[n] = '1'

        else:
            new_chrom[n] = '0'

        population[l[i]] = ''.join(new_chrom)
    return population

        
def cross1(chrom1, chrom2):
    half = len(chrom1) // 2
    new_chrom1 = []
    new_chrom2 = []
    for i in range(0, half):
        new_chrom1.append(chrom2[i])
        new_chrom2.append(chrom1[i])

    for i in range(half, len(chrom1)):
        new_chrom1.append(chrom1[i])
        new_chrom2.append(chrom2[i])
    return ''.join(new_chrom1), ''.join(new_chrom2)

def cross2(chrom1, chrom2):
    new_chrom1 = []
    new_chrom2 = []

    for i in range(len(chrom1)):
        p = randint(0,1)
        if p == 0:
            new_chrom1.append(chrom1[i])
            new_chrom2.append(chrom2[i])
        else:
            new_chrom1.append(chrom2[i])
            new_chrom2.append(chrom1[i])
    return ''.join(new_chrom1), ''.join(new_chrom2)




print(cross2('100111', '111011'))


#print(generate_population(100))

#n_population: number of chroms
#n_mutation: mutation rate
#t_crossover: type of crossover
#t_mutation: type of mutation
#n_iterations: number of iterations
#n_elitism: elitism rate

def genetic(n_population, n_mutation, t_crossover,  t_mutation, n_iterations, n_elitism):
    return None