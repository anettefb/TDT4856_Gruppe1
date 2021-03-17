from files import file_handling, measurements
from pattern import *
from data_prep import *

"""dict_wheel = {
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
}"""

# General information
DATA_START = 80.0
DATA_END = 100.0
UNIT = "mm"
MIDANGLE = (DATA_START-DATA_END)/2
WINTER_THRESHOLD = 5 #mm
SUMMER_THRESHOLD = 1.6 #mm


def main():
    file_handling()
    data = extract_info(measurements)
    t_data = trig(data)
    pattern_depth, edges, pattern = pattern_positions(data)
    ver = check_pattern(pattern_depth, WINTER_THRESHOLD)
    
    #print(f"PATTERN (angles): {pattern}")
    #print(f"Edges (angle): {edges}")
    
    print("""██████  ███████ ███████ ██    ██ ██   ████████
██   ██ ██      ██      ██    ██ ██      ██    ██
██████  █████   ███████ ██    ██ ██      ██
██   ██ ██           ██ ██    ██ ██      ██    ██
██   ██ ███████ ███████  ██████  ███████ ██
                                                """)
    print(f"Pattern depth: {pattern_depth}")
    print(f"Is the tire approved: {ver}\n")



if __name__ == "__main__":
    main()
    


