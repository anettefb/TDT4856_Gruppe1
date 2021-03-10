import collections
 
DATA_START = 83.0
DATA_END = 97.0
    

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
    
