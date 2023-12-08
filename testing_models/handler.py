from Generation import Generation

def run_selection(has_weighted_reproduction, has_uniform_crossover, has_pair_reproduction, has_selection):
    
    first_generation += Generation(
                            has_weighted_reproduction, 
                            has_uniform_crossover, 
                            has_pair_reproduction, 
                            has_selection, 
                            is_first_generation=True
                        )]
    

    general_fittest = [first_generation.fittest()]
    general_fit     = [generation[0].avg_fit()]

    count_fitness_decrease      = 0
    count_fitness_repetitions   = 0
    count_small_fitness_changes = 0

    current_generation = first_generation
    while(True):

        previous_generation  = current_generation

        current_generation   = current_generation.get_next()

        previous_fittest     = previous_generation.fittest()

        fit_data = current_generation.get_fit_data()
        current_fittest, current_avg_fit = fit_data

        general_fittest     += [current_fittest]
        general_fit         += [current_avg_fit]


        if(current_fitness <= previous_fitness):
            count_fitness_decrease += 1
        
        fitness_ratio = current_fitness / previous_fitness
        if((fitness_ratio >= 0.99) and (fitness_ratio >= 1.01)):
            count_small_fitness_change += 1

        count_fitness_repetitions = generation.count(current_generation)


        first_condition    = count_fitness_decrease     < 5
        second_condition   = count_small_fitness_change < 5
        third_condition    = count_fitness_repetitions  < 3

        if(     not first_condition
            or  not second_condition
            or  not third_condition):

            return (general_fittest, general_fit)
