def pattern_positions(pattern_dictionary):
    """ Will find the position of the different patterns and return a dictionary containing
    that info """
    dict_pattern_position  = {
    }
    prev_key = next(iter(pattern_dictionary))
    main_key = next(iter(pattern_dictionary))
    count = 0
    num = 0
    pattern = False
    
    for key in pattern_dictionary:
        possible_dist = pattern_dictionary[main_key]-pattern_dictionary[key]
        if pattern_dictionary[main_key]-pattern_dictionary[key] < pattern_dictionary[main_key]-pattern_dictionary[prev_key]:
            main_key = key
            pattern = False
        elif pattern_dictionary[key] < pattern_dictionary[main_key] : #and possible_dist > 1.8
            count += 1
            pattern = True
            print(count)
            if count > 2:
                #print("IT'S a pattern!!!!")
                k=1
            else:
                #print("NOT")
                k=2
        elif pattern_dictionary[key] >= pattern_dictionary[main_key] : #and possible_dist < 1.8
            pattern = False
            main_key = key
            count = 0
            
        #print(prev_key, "\n", main_key)
        prev_key = key
        print(pattern)
        

        
        
            
        """
            val += pattern_dictionary[key]
            num += 1
            print(val, "\n", num)
        prev_key = key
        print(prev_key)
        """
        
        




dict = { 75.2: 500,
75.4: 495,
75.8: 496,
78: 495,
79: 502,
80: 501,
81: 502,
82: 501,
83: 494,
84: 494,
85: 494,
86: 494,
87: 500,
88: 500,
89: 500,
90: 500,
}
    
DATA_START = 80.0
DATA_END = 100.0
UNIT = "mm"

pattern_positions(dict)

""" Must calculate the difference in distance"""



