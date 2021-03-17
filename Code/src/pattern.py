def pattern_positions(pattern_dictionary):
    """ Will find the position of the different patterns and return a list
with the angles (keys) where the pattern is. It also returns the end
edges of the pattern for calculating the depth.
"""
    count = 0
    threshold = 1.79
    pattern_threshold = 1

    prev_key = list(pattern_dictionary.keys())[0]
    main_key = list(pattern_dictionary.keys())[0]

    max = 0
    edges = []
    angles = []
    depth_pattern = []

    for key in pattern_dictionary:

        if pattern_dictionary[key] < pattern_dictionary[prev_key] and \
                pattern_dictionary[prev_key] - pattern_dictionary[key] > threshold:
            if prev_key in angles:
                edges.append(key)
                d = max - (pattern_dictionary[key]+pattern_dictionary[main_key])/2 #tar gjennomsnitt av kantene for å få mest mulig riktig svar (forhindrer skjevhet i dataen)
                depth_pattern.append(d)
            count = 0
            main_key = key
            max = 0

        elif pattern_dictionary[key] > pattern_dictionary[main_key] and \
                pattern_dictionary[key] - pattern_dictionary[main_key] > threshold:
            count += 1
            if count >= pattern_threshold:
                if pattern_dictionary[key] > max:
                    max = pattern_dictionary[key]
                    
                angles.append(key)
                if count == pattern_threshold and main_key not in edges:
                    edges.append(main_key)
                    
        else:
            if prev_key in angles:
                edges.append(key)
                d = max - (pattern_dictionary[key]+pattern_dictionary[main_key])/2
                depth_pattern.append(d)

            main_key = key
            count = 0
            max = 0
        prev_key = key
        

    return depth_pattern, edges, angles


def check_pattern(depth, threshold):
    approved = []
    for item in depth:
        if item > threshold:
            approved.append("Yes")
        else:
            approved.append("No")
    return approved
