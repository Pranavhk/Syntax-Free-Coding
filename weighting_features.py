import data_store as ds
import numpy as np
from collections import Counter

def modify_weights(freq_dict, sent_dict):
    temp_freq_dict = freq_dict.copy()
    for key,values in temp_freq_dict.items():
        ns = sent_dict[key] # total number of sentences of the class 'key'
        type(values)
        for w,v in values.items():
            nsw = values[w] # number of sentences of a class values containing word v
#            if(ns == nsw):
#                ns = _get_total_sentences(sent_dict)
#                nsw = _get_total_sentences_feature(w, freq_dict)
            idf_weight =  int(np.ceil(np.log(1 + (ns/nsw))))
            values[w] = values[w]*idf_weight

    for key in temp_freq_dict.keys():   
        ds.data_to_json(key, Counter(temp_freq_dict[key]), 'weighted_freq.json')

#    ds.data_to_json()        
    
 
