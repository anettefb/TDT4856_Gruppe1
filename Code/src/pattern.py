def pattern_positions(pattern_dictionary):
    """ Will find the position of the different patterns and return a list
with the angles (keys) where the pattern is. It also returns the starting
edges of the pattern for calculating the depth.
"""
    count = 0
    threshold = 1.8
    pattern_threshold = 1

    prev_key = list(pattern_dictionary.keys())[0]
    main_key = list(pattern_dictionary.keys())[0]

    c = 0
    edges_end = []
    angles = []
    depth_pattern = []

    for key in pattern_dictionary:

        if pattern_dictionary[key] < pattern_dictionary[prev_key] and \
                pattern_dictionary[prev_key] - pattern_dictionary[key] > threshold:
            if prev_key in angles:
                edges_end.append(key)
                d = c/count - pattern_dictionary[main_key]
                print(d)
                depth_pattern.append(d)
            count = 0
            main_key = key
            c = 0

        elif pattern_dictionary[key] > pattern_dictionary[main_key] and \
                pattern_dictionary[key] - pattern_dictionary[main_key] > threshold:
            count += 1
            if count >= pattern_threshold:
                c += pattern_dictionary[key]
                angles.append(key)
                print(c)
                print(count)
            if key == list(pattern_dictionary.keys())[-1]:
                depth_pattern.append(pattern_dictionary[key] - pattern_dictionary[main_key])
        else:
            if prev_key in angles:
                edges_end.append(key)
                d = c/count - pattern_dictionary[key]
                print(d)
            main_key = key
            count = 0
            c = 0
        prev_key = key

    return depth_pattern, edges_end, angles


def check_pattern(depth):
    threshold = 5
    approved = []
    for item in depth:
        if item > threshold:
            approved.append("Yes")
        else:
            approved.append("No")
    return approved
