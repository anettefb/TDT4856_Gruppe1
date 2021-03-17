import collections
import numpy as np
 
DATA_START = 83.0
DATA_END = 100.0
THRESHOLD = 3.0

def extract_info(measurement_dict):
    global DATA_START
    global DATA_END
    global THRESHOLD
    
    wanted_data = {}
    prev_key = None
    
    for key in measurement_dict:
        if key < DATA_START or key > DATA_END:
            continue
            
        if prev_key == None:
            prev_key = key
            continue
            
        if abs(measurement_dict[prev_key] - measurement_dict[key]) < THRESHOLD:
            wanted_data[key] = measurement_dict[key]
        
        prev_key = key
        
        
    
    sorted_dict = dict(collections.OrderedDict(sorted(wanted_data.items())))
    
    return sorted_dict
    
def trig(data):
    
    list_data = list(data.keys())
    mid = list_data[len(list_data)//2]

    for key in data:
        data[key] = data[key]*np.cos(np.deg2rad(key-mid))
    
    return data
