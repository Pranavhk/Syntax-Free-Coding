import nltk
import logging
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from ordered_set import OrderedSet


var_keywords = ['variables', 'variable']
val_keywords =[ 'value', 'values']

tag_NN_list =['DT', 'NN','NNS','NNPS','RBR','NNP','RB']

def preprocess_text_nb_classifier(sentence):
    sentence = sentence.replace(","," , ")
    literals, numerals,semi_feature_bag=_get_literals_numerals(sentence)
    sentence_word_list = remove_stopwords(" ".join(semi_feature_bag))  
    feature_bag = stemm_features(sentence_word_list)
    #print(feature_bag)
    return literals,numerals,feature_bag

def remove_stopwords(sentence) :
    sentence = sentence.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(sentence)
    filtered_words = [w for w in tokens if not w in nltk.corpus.stopwords.words('english')]
    return (filtered_words)


def stemm_features(feature_bag) :
    porter = PorterStemmer()
    stemmed = list()
    for word in feature_bag:
        stemmed.append(porter.stem(word))
    return stemmed

def _get_literals_numerals(sentence) :
    literals,numerals = list(), list()
    token_tag_list = nltk.pos_tag(nltk.word_tokenize(sentence))
    token_no_literals_list = list()
    token_no_var_list = list()
    word_list = sentence.split(' ')
    for word,tag in token_tag_list:
        if((tag == 'CD')) :
            if(word.isdigit()) :
                numerals.append(word)
        else :
            token_no_literals_list.append(tuple([word,tag]))
    i = 0
    omit = -1
    for i in range(0,len(token_no_literals_list)):
        if i > omit :
            if(token_no_literals_list[i][0] in var_keywords):
                try:
                    token_no_var_list.append(token_no_literals_list[i][0])
                    #print(token_tag_list[i][0])
                    #print(token_tag_list[i+1][1], token_tag_list[i+1][0])
                    if (token_no_literals_list[i+1][1] in tag_NN_list):
                        literals.append(token_no_literals_list[i+1][0])
                        omit = i+1
                        temp_list = token_no_literals_list[i+2:]
                        for j in range(0, len(temp_list)):
                            tag1 = temp_list[j][1]
                            word1 = temp_list[j][0]
                            if (word1 == ','):
                                literals.append(temp_list[j+1][0])
                                temp_list.pop(j+1)
                                omit = omit + 2
                            elif (tag1 == 'CC' or tag1 == 'IN' or tag1 == 'TO'):
                                if(temp_list[j+1][0] not in val_keywords):
                                    literals.append(temp_list[j+1][0])  
                                    omit = omit + 2
                                    break
                            else:
                                break
                except :
                    pass
            else:
                token_no_var_list.append(token_no_literals_list[i][0])

    literals = list((OrderedSet(literals)))
    #print(literals, numerals)
    return literals, numerals,token_no_var_list