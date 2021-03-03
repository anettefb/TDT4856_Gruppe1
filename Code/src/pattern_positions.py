def pattern_positions(pattern_dictionary):
    """ Will find the position of the different patterns and return a list
with the angles (keys) where the pattern is. It also returns the starting 
edges of the pattern for calculating the depth. 

"""
    count = 0
    threshold = 1.8

    prev_key = next(iter(pattern_dictionary))
    main_key = next(iter(pattern_dictionary))

    edges = []
    angles = []


    for key in pattern_dictionary:
        if pattern_dictionary[key] < pattern_dictionary[main_key] and pattern_dictionary[main_key] - \
                pattern_dictionary[key] > threshold:
            count += 1

            if count == 2:
                # edge_start!
                angles.append(prev_key)
                angles.append(key)
                edges.append(main_key)

            if count > 2:
                angles.append(key)

        else:
            main_key = key
            count = 0

        prev_key = key

    #print(angles)
    #print(edges)
    return angles, edges
