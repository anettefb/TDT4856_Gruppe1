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
        if pattern_dictionary[key] > pattern_dictionary[prev_key] and pattern_dictionary[key] - \
                pattern_dictionary[prev_key] > threshold:
            is_pattern = False
            main_key = key
            count = 0
        elif pattern_dictionary[key] < pattern_dictionary[main_key] and pattern_dictionary[main_key] - \
                pattern_dictionary[key] > threshold:
            count += 1
            is_pattern = True
            print(count)

            if count == 2:
                # edge_start!
                angles.append(prev_key)
                angles.append(key)

            if count > 2:
                angles.append(key)

        elif pattern_dictionary[key] >= pattern_dictionary[main_key]:
            is_pattern = False
            main_key = key
            count = 0

        prev_key = key
    #print(angles)
    #print(edges)
    return angles
