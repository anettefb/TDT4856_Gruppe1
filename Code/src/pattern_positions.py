def pattern_positions(pattern_dictionary):
    """ Will find the position of the different patterns and return a list
with the angles (keys) where the pattern is. It does not include the edges,
just the values for the positions where the depth differs from 

"""
    count = 0
    threshold = 1.8

    prev_key = next(iter(pattern_dictionary))
    main_key = next(iter(pattern_dictionary))

    edges = []
    angles = []
    is_pattern = False

    for key in pattern_dictionary:
        if pattern_dictionary[key] < pattern_dictionary[main_key] and \ pattern_dictionary[main_key] - pattern_dictionary[key] > threshold:
            count += 1
            is_pattern = True

            if prev_key == main_key:
                edges.append(prev_key)

            if count == 2:
                # edge_start!
                angles.append(prev_key)
                angles.append(key)

            if count > 2:
                angles.append(key)
                
        else:
            main_key = key
            count = 0

        prev_key = key
        print(main_key)
    #print(angles)
    #print(edges)
    return angles, edges
