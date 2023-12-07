def generate_parameters():

    has_weighted_reproduction   = True  
    has_uniform_crossover       = True  
    has_pair_reproduction       = True  
    has_selection               = True  

    first_test_parameters = [               
        has_weighted_reproduction   == False,
        has_uniform_crossover       == False,
        has_pair_reproduction       == False,
        has_selection               == False 
    ]

    second_test_parameters = [              
        has_weighted_reproduction   == True , 
        has_uniform_crossover       == False,
        has_pair_reproduction       == False,
        has_selection               == False,
    ]

    third_test_parameters = [               
        has_weighted_reproduction   == True,
        has_uniform_crossover       == False,
        has_pair_reproduction       == True,
        has_selection               == False 
    ]

    fourth_test_parameters = [              
        has_weighted_reproduction   == True,
        has_uniform_crossover       == False,
        has_pair_reproduction       == True,
        has_selection               == True  
    ]

    fith_test_parameters = [                
        has_weighted_reproduction   == False,
        has_uniform_crossover       == True,
        has_pair_reproduction       == False,
        has_selection               == False 
    ]

    sixth_test_parameters = [               
        has_weighted_reproduction   == True,
        has_uniform_crossover       == True,
        has_pair_reproduction       == False,
        has_selection               == False 
    ]

    seventh_test_parameters = [             
        has_weighted_reproduction   == True,
        has_uniform_crossover       == True,
        has_pair_reproduction       == True,
        has_selection               == False 
    ]

    eighth_test_parameters = [              
        has_weighted_reproduction   == True,
        has_uniform_crossover       == True,
        has_pair_reproduction       == True,
        has_selection               == True  
    ]

    return [
            first_test_parameters,
            second_test_parameters,
            third_test_parameters,
            fourth_test_parameters,
            fith_test_parameters,
            sixth_test_parameters,
            seventh_test_parameters,
            eighth_test_parameters,
    ]
