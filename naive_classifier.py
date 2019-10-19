import nltk
import logging
import data_store as dbutil
from collections import Counter
import preprocessing
import Translator_basic as tb
import reading_Data
import weighting_features as wf
import os

bagwords = list()
results = dict()

new_weight_file = 'weighted_freq.json'
freq_dist_file = 'nlpdata.json'

def nb_classifier(sentence,f) :
    #cl_sentence = preprocessing(sentence)
    literals, numerals,feature_words = preprocessing.preprocess_text_nb_classifier(sentence)
    
    counter = dbutil.intent_count(new_weight_file)

    intent_collection = dbutil.json_to_data(new_weight_file)
    for count in range(counter) :
        intent_words = Counter()
        intent_words["positive"] = Counter()
        intent_words["negative"] = Counter()
        i=0
        for key,value in sorted(intent_collection.items()):
            if i == count :
                intent_words["positive"] = Counter(value)
                #print("{} classifier running".format(key))
                intent = key
            else :
                intent_words["negative"] = intent_words["negative"] + Counter(value)
            i = i+1
        bagwords = list(intent_words["positive"].keys()) + list(intent_words["negative"].keys())
        results[intent] = list(bayes_classify(feature_words,intent_words,intent))
    
    result_intent = keywithmaxval(results)
    # print("The Operation is {}".format(result_intent))
    new_data = Counter(nltk.FreqDist(feature_words))
    # print(literals,numerals)
    tb.translator_input(result_intent, numerals, literals,f)
    if (result_intent == 'while'):
       tb.looped = 1   
    if (result_intent == 'stop'):
        tb.looped = 0 
    reading_Data.class_statements_count[result_intent] += 1

     #need to be changed with preprocessed string
    dbutil.data_to_json(result_intent,new_data, freq_dist_file)
    temp = dbutil.json_to_data(freq_dist_file) 
    wf.modify_weights(temp, reading_Data.class_statements_count)
    return result_intent


def keywithmaxval(d):  
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]
            
                    
def bayes_classify(feature_words, intent_dict1,intent):
    class1, class2 = intent_dict1.keys()
    set_words = feature_words
    p1 = get_class_prob(set_words, class1, intent_dict1)
    p2 = get_class_prob(set_words, class2, intent_dict1)
    #print("{} : {} , not {}: {}".format(intent,p1,intent,p2))
    return p1,p2

def get_class_prob(set_words,class_,intent_dict1):
    intent_dict = intent_dict1.copy()
    class1 = class_
    total1 = len(list(set(bagwords)))
    #print(bagwords,total1)
    i1 =0
    for word in set_words:
        total1 = len(list(set(bagwords)))
        if word in intent_dict[class1]:
            intent_dict[class1][word] += 1
            p_word = (intent_dict[class1][word])/((total1+1) + len(intent_dict[class1].keys()))
            i1 = i1+1
        else:
            p_word= (1)/((total1+1) + len(intent_dict[class1].keys()))
            i1 = i1+1
        if(i1 == 1):
            p = p_word
        else:
            p = p * p_word
        bagwords.append(word)
    return p


#nb_classifier('assign variable variable_1 to sum')
#nb_classifier("Print hello world")

## DO NOT DELETE: Program to calculate sum of n numbers
'''nb_classifier("Initialize a variable sum with value 0")
nb_classifier('Iterate a loop for variable i from 50 to 5')
nb_classifier('Add the variable i with sum')
nb_classifier('Assign variable variable_1 to sum')
nb_classifier("Decrement variable i by 1")
nb_classifier('stop the loop')
nb_classifier('Display the variable sum')'''

#nb_classifier("Add value 1 and 2")
#nb_classifier("Assign variable variable_1 to sum")