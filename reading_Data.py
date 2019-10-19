import sys
import preprocessing
from collections import Counter
import data_store as dbutil
import nltk
import weighting_features 
CLASSES_ = ['initialize', 'print', 'add', 'subtract', 'divide', 'while', 'multiply', 'divide', 'stop']

class_statements_count = dict(zip(CLASSES_, [0]* len(CLASSES_)))

def read_data():
    pass

if __name__ == "__main__":

    path=(r"/home/pranav/Downloads/30th May 2019/Intent_Collection")
    with open(path, mode='r') as f:
        data =f.readlines()
        l= [s.rstrip('\n') for s in data]
        ll = list()
        for d in l:
            try:
                temp = d.split('$')
                (x,y)= temp[0], temp[1]
                t = x.split('.')
                y = y.strip()
                x = t[0]
            except:
                continue
            ll.append((x,y))
    #        print(ll)
        
    for x,y in ll:
        try:
            x = x.lower()
            print(x)
            l,n,f_bag = preprocessing.preprocess_text_nb_classifier(x)
            new_data = Counter(nltk.FreqDist(f_bag))
            dbutil.data_to_json(y.lower(),new_data, "nlpdata.json")
            class_statements_count[y.lower()] += 1 
        except:
            print(x)

    s = dbutil.json_to_data('nlpdata.json')
    #print(s)
    weighting_features.modify_weights(s, class_statements_count)
    #wf.modify_weights
    read_data()

