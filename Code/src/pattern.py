def pattern_positions(pattern_dictionary):
    """ Will find the position of the different patterns and return a list
with the angles (keys) where the pattern is. It also returns the starting 
edges of the pattern for calculating the depth.
"""
    count = 0
    threshold = 1.8
    pattern_threshold = 2

    prev_key = next(iter(pattern_dictionary))
    main_key = next(iter(pattern_dictionary))
    
    d = 0

    edges = []
    angles = []
    depth_pattern = []

    for key in pattern_dictionary:
        if pattern_dictionary[key] < pattern_dictionary[main_key] and pattern_dictionary[main_key] - \
                pattern_dictionary[key] > threshold:
            count += 1

            if count == pattern_threshold:
                # edge_start!
                angles.append(prev_key)
                angles.append(key)
                edges.append(main_key)
                d += pattern_dictionary[prev_key]
                d += pattern_dictionary[key]

            if count > pattern_threshold:
                angles.append(key)
                d += pattern_dictionary[key]
            #print(d)
                

        else:
            if prev_key in angles:
                c = pattern_dictionary[main_key] - d/count
                depth_pattern.append(c)
                d = 0
            
            main_key = key
            count = 0
            
        prev_key = key

    #print(angles)
    #print(edges)
    return angles, edges, depth_pattern


def check_pattern(depth):
    threshold = 5
    approved = []
    for item in depth:
        if item > threshold:
            approved.append("Yes")
        else:
            approved.append("No")
    return approved
