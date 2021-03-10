from files import file_handling, measurements
from pattern import *
from data_prep import *

dict_wheel = {
79.1: 502,
80.1: 501,
81.1: 502,
82.1: 501,
83.1: 494,
84.1: 494,
85.1: 494,
86.1: 494,
87.1: 500, #mønster
89.1: 500.01, #mønster
90.1: 498,
91.1: 498,
92.1: 498,
93.1: 500,
94.1: 500,
95.1: 502, #mønster
96.1: 494,
97.1: 494,
98.1: 495,
88.1: 500,
99.1: 500,
100.1: 500,
101.1: 501,
}

# General information
DATA_START = 80.0
DATA_END = 100.0
UNIT = "mm"
MIDANGLE = (DATA_START-DATA_END)/2
WINTER_THRESHOLD = 5 #mm
SUMMER_THRESHOLD = 1.6 #mm



    
"""
def triangulate_measurements(measurement_dict):
    DATA_START = 80.0
    DATA_END = 100.0
    mid_angle = (DATA_END-DATA_START)/2
    
    useful_dict = {}
    
    for key in measurement_dict:
    
"""
    



"""


#run functions
pattern, start_edges, pattern_depth = pattern_positions(dict_wheel) # finding the postitions for mønsteret
ver = check_pattern(pattern_depth)

print(pattern_depth,"\n")

print(ver)

"""


def main():
    file_handling()
    #print(measurements)
    data = extract_info(dict_wheel) # measurements - ekte data
    #print(data)

    pattern_depth, end_edges, pattern = pattern_positions(data) # finding the postitions for mønsteret
    ver = check_pattern(pattern_depth)
    
    print(f"PATTERN: {pattern}")
    print(f"Edges: {end_edges}")
    
    print(f"Pattern depth: {pattern_depth}")
    print(ver)



if __name__ == "__main__":
    main()
    


