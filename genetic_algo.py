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

# function cross 1 take half of the chromossome and switch wiht another chrom
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

#cross uniform function: take a probability of 50% to switch a gene
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


#function calculate_fit test all restritions
def calculate_fit(chrom):
    fit = 0

    restritions = [restrition1, restrition2, restrition3, restrition4]

    for i in restritions:
        fit+=i(chrom)
    
    return fit




print(cross2('100111', '111011'))


#print(generate_population(100))

#n_population: number of chroms
#n_mutation: mutation rate
#t_crossover: type of crossover
#t_mutation: type of mutation
#n_iterations: number of iterations
#n_elitism: elitism rate




def genetic1(population, n_mutation, t_crossover,  t_mutation, n_iterations, n_elitism, n, k):
    if t_crossover == 0:
        cross = cross1
    else:
        cross = cross2

    if t_mutation == 0:
        mutation = mutation0
    else:
        mutation = mutation1
    
    for i in range(n_iterations):
        cross_population = []
        fit_cross_population = []

        if len(population) % 2 == 0:
            for w in range(0, len(population), 2):
                chrom1 = population[w]
                chrom2 = population[w+1]

                chrom1, chrom2 = cross(chrom1, chrom2)

                cross_population.append(chrom1)
                cross_population.append(chrom2)

                fit_cross_population.append()


