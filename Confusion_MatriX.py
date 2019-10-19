#READ ME:
#Independant file 
#Changes to be made- 1. Comment translator call in nb_classifier 2. Return intent 



#%%
import numpy as np
import csv, glob, os, naive_classifier
import sklearn, matplotlib
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn import datasets, naive_bayes, svm
from sklearn.metrics import confusion_matrix, accuracy_score,precision_score,recall_score
from sklearn.model_selection import train_test_split
#path = ( r"C:\Users\USER\Desktop\Project\B.E. Project\UB\Naive_Bayes_Classifier\Train.csv")
#%%
f = open("test.csv", 'r')
'''fields = [] 
rows = [] 
#X = csvfile.data()
Y = csvfile.target()
# Split the data into a training set and a test set
#X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0)


df = pd.DataFrame(np.random.randn(100, 2))

msk = np.random.rand(len(df)) < 0.8

train = df[msk]

test = df[~msk]

train, test = train_test_split(filename, test_size = 0.2)
labels = ['TP','TN']
classifier = svm.SVC(kernel='linear',C=0.001)
#cm = confusion_matrix(test_obs, test_pred, labels)

df = pd.read_csv(filename,error_bad_lines=False)
#df = pd.concat(map(pd.read_csv, glob.glob(os.path.join("Train.csv", error_bad_lines ="False" ))))
X = df.drop('Y', axis=1)
y = df['Y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40)
X_train = X_train.drop('time', axis=1)
X_test = X_test.drop('time', axis=1)
index_values=range(0,len(y_test))
y_test.sort_index(inplace=True)
X_test.sort_index(inplace=True)
modelPred_test = reg.predict(X_test)
ax.plot(pd.Series(index_values), y_test.values)

test_true = ['Add','Subtract','Initialize','Stop','While']
test_pred = ['Add','Subtract','While','Stop','While']
cm = confusion_matrix(test_true,test_pred)
plt.imshow(cm, cmap='binary', interpolation='None')
plt.show()
ac = accuracy_score(test_true,test_pred)
print(ac)
'''

'''
Find the division of variable X and variable Y.
Determine the multiplication of variables X and B.
Create variables m, j and k with values 10, 12 and 2312.
Iterate a loop for variable l from 1 to 23.
,'multiply','divide','Initialize','while'
'''



test_true = []
test_pred = ['stop','stop','divide','divide','multiply','multiply','subtract','subtract','add','add','while','while','Print','Print','Initialize','Initialize','Initialize','multiply','divide','Initialize','while']
 
#%%
line = f.readline()
#%%
while line:
    x = naive_classifier.nb_classifier(line,f)
    test_true.append(x)
    line = f.readline()

f.close() 
#%%   
cm = confusion_matrix(test_true,test_pred)
plt.imshow(cm, cmap='binary', interpolation='None')
plt.show()

ac = accuracy_score(test_true,test_pred)
s = str(ac)
print("Accuracy: "+s)
pr = precision_score(test_true,test_pred,average='macro')
s1 = str(pr)
print("Precision is: "+s1)
rc = recall_score(test_true,test_pred,average='macro')
s2 = str(rc)
print("Recall is: "+s2)



	

#%%
