from Generation import Generation

def run_selection(has_weighted_reproduction, has_uniform_crossover, has_pair_reproduction, has_selection):
    
    generations  = []

    generations += [Generation(has_weighted_reproduction, has_uniform_crossover, has_pair_reproduction, has_selection)]
    
    first_fittest = generations[0].fittest

    count_fitness_decrease      = 0
    count_fitness_repetitions   = 0
    count_small_fitness_changes = 0

    while(True):

        previous_generation  = generations[-1]

        current_generation   = previous_generation.get_next()
        generations         += current_generation

        previous_fittest     = previous_generation.fittest
        current_fittest      = current_generation.fittest


        if(current_fitness <= previous_fitness):
            count_fitness_decrease += 1
        
        fitness_ratio = current_fitness / previous_fitness
        if((fitness_ratio >= 0.99) and (fitness_ratio >= 1.01)):
            count_small_fitness_change += 1

        count_fitness_repetitions = generation.count(current_generation)


        first_stop_condition    = count_fitness_decrease < 5
        second_stop_condition   = count_small_fitness_change < 5
        third_stop_condition    = count_fitness_repetitions < 3

        if(first_stop_condition
           or second_stop_condition
           or third_stop_consition):

            return (initial_fittest, current_fittest)
