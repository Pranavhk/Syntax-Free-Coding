
#%%
sentence = '''Initialize a variable with values 2 and 3 . 
Assign variables 2,4 and 3 to three variables. 
Mark values 2 and 3 as values for two variable. 
Create variables a,b and c with values 2,5 and 3. 
Alot two variables with values 2 and 3. 
Form two variables with values with 2 and 3. 
Take two variables with values 2 and 3. 
Appoint value 2 and 3 to two variable. 
Delegate value 2 and 3 to two variable. 
enerate two variables with values 2 and 3. 
Give value 2 and 3 as value to two variable.
Construct two variables with values 2 and 3.
Set up two variables with value 2 and 3.
Establish two variables with values 2 and 3.
Produce two variables with values 2 and 3. 
Compose two variables with values 2 and 3.  
Print the variable P.
Print the variable C and D.
Display the result for variable X.
Show the result of variable X.
Exhibit the result for variable X.
Present the answer for variable X.
Resolve the answer for variable X.
Actuate the result for variable X.
Cinch the result for variable X. 
Reveal the answer for variable X. 
Iterate a variable from value 1 until 100.
Form a loop to iterate a variable from 1 to 10.
Range a variable from value 1 over 100. 
Make a variable to loop from 1 to 10.
Loop over a variable 10 times. 
Create a loop that runs from 1 to 10.
Iterate a variable from 1 to 10.
Run a loop from 1 to 100. 
Give the sum of two variable X and Y.
Take variables X and Y and add them.
Determine the addition of two variable X and Y.
Find the result after adding two variable X and Y.
Calculate the sum of two variable X and Y. 
Find the sum of two variable X and Y.
Reckon two variable X and Y.
Give the total of numbers from 1 to 10.
Formulate the result after adding variable X and Y.
First Variable plus second variable.
Calculate variable X plus Y.
Subtract the numbers X and Y.
Give the subtraction of two variable X and Y. 
Take these variable X & Y and subtract them.
Determine the Subtraction of two variable X and Y.
Find the result after Subtracting X and Y.
Compute the Subtraction of two numbers X and Y. 
Calculate the difference between X and T.
X minus Y.
Find the result if A is multiplied by B.
Multiply X with Y.
Multiply two numbers X and Y.
Find the multiplication of X and Y. 
Calculate the result of by multiplying X and Y.
Determine the multiplication of variable X and B.
Evaluate the multiplication of X and Y.
Solve for X multiplied by Y.
Find the result if A is multiplied by B.
Multiply X with Y.
Divide two variable X and Y.
Solve for X divided by Y.
Find the result if A is divided by B.
Divide X by Y.
Divide two variable X and Y.
Find the division of X and Y.
Calculate the result of by dividing X and Y.
'''


#%%
sentence


#%%
sentence = sentence.replace("\n"," ")
sentence


#%%
sentence = sentence.replace(","," , ")
sentence = sentence.replace("."," . ")
sentence


#%%
#Till here is common


#%%
#this is for training data
training_doc = sentence
training_doc = training_doc.replace(".", "")
no_literals_list = list()
token_train_list = nltk.pos_tag(nltk.word_tokenize(training_doc))
for word,tag in token_train_list:
        if(not tag == 'CD'):
            no_literals_list.append(word)
            
no_literals_list


#%%
import nltk
rights = "Add numbers 1 and numbers 2"
token_tag_list = nltk.pos_tag(nltk.word_tokenize(rights))
token_tag_list


#%%
from nltk.tokenize import RegexpTokenizer
from ordered_set import OrderedSet
from nltk.stem import PorterStemmer
LITERALS = list()
NUMERALS = list()
var_keywords = ['variables', 'variable']
val_keywords =[ 'value', 'values']

tag_NN_list =['DT', 'NN','NNS','NNPS','RBR','NNP','RB']

def preprocess_text_nb_classifier(sentence):
    sentence = sentence.replace(","," , ")
    literals, numerals,semi_feature_bag=_get_literals_numerals(sentence)
    LITERALS.append([literals, numerals, sentence])
    sentence_word_list = remove_stopwords(" ".join(semi_feature_bag))  
    feature_bag = stemm_features(sentence_word_list)
     #only removing literals with/without stemming
#    print(sentence,sentence_word_list,'\n','Literals_saved:',literals,'\n',feature_bag)
    #print(feature_bag)
    return feature_bag

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
    flag ="none"
    for i in range(0,len(token_no_literals_list)):
        if i > omit :
            if(token_no_literals_list[i][0] in var_keywords):
                token_no_var_list.append(token_no_literals_list[i][0])
                flag =0
                #print(token_tag_list[i][0])
                #print(token_tag_list[i+1][1], token_tag_list[i+1][0])
                if (token_no_literals_list[i+1][1] in tag_NN_list):
                    literals.append(token_no_literals_list[i+1][0])
                    omit = i+1
                    flag ="var_f"
                    print(flag)
                    temp_list = token_no_literals_list[i+2:]
                    for j in range(0, len(temp_list)):
                        tag1 = temp_list[j][1]
                        word1 = temp_list[j][0]
                        if (word1 == ','):
                            literals.append(temp_list[j+1][0])
                            temp_list.pop(j+1)
                            omit = omit + 2
                            flag ="com_f"
                            print(flag)
                        elif (tag1 == 'CC' or tag1 == 'IN' or tag1 == 'TO'):
                            if(temp_list[j+1][0] not in val_keywords):
                                literals.append(temp_list[j+1][0])  
                                omit = omit + 2
                                flag ="CC found"
                                print(flag)
                                break
                        else:
                            break
            else:
                token_no_var_list.append(token_no_literals_list[i][0])

    print(" ".join(token_no_var_list)  )  
    literals = list((OrderedSet(literals)))
    print(literals, numerals)
    return literals, numerals,token_no_var_list


#%%
preprocess_text_nb_classifier("Add numbers 1 and numbers 2")


#%%
import numpy
print(numpy.__path__)


#%%



#%%



