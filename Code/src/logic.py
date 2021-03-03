from pattern_positions import pattern_positions

dict_wheel = { 74: 500,
75: 496,
76: 495,
77: 496,
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
90: 498,
91: 498,
92: 498,
93: 500,
}
    
DATA_START = 80.0
DATA_END = 100.0
UNIT = "mm"

pattern, start_edges, pattern_depth = pattern_positions(dict_wheel) # finding the postitions for mønsteret

print(pattern_depth)
print()

"""
def calculate_pattern_depth(start_key, pattern_key, dictionary):
    
    depth = []
    
    for key in dictionary:
        
        for item in pattern_key:
            
"""





