import collections
import numpy as np
 
DATA_START = 83.0
DATA_END = 96.0
    

def extract_info(measurement_dict):
    global DATA_START
    global DATA_END
    
    wanted_data = {}
    
    for key in measurement_dict:
        if key < DATA_START or key > DATA_END:
            continue
            
        wanted_data[key] = measurement_dict[key]
    
    sorted_dict = dict(collections.OrderedDict(sorted(wanted_data.items())))
    
    return sorted_dict
    
def trig(data):
    #print(data)
    list_data = list(data.keys())
    #print(list_data)
    mid = list_data[len(list_data)//2]
    #print(mid)
    for key in data:
        data[key] = data[key]*np.cos(np.deg2rad(key-mid))
    
    return data
