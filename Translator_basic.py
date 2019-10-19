#%%
from collections import deque
import os;
used_variables = []
result_variables = []
temp = []
variable_list = deque(['variable_1','variable_2','variable_3','variable_4','variable_5','variable_6','variable_7','variable_8','variable_9','variable_10'])
looped = 0

#%%
def translator_input(intent, literals, variables,f):
    #try:   
        if(intent == "initialize"):
            initialize(literals,variables,f)
        elif (intent == 'add'):
            add(literals,variables,f)
        elif (intent == 'subtract'):
            subtract(literals,variables,f)
        elif (intent == 'multiply'):
            multiply(literals,variables,f)
        elif (intent == 'divide'):
            divide(literals,variables,f)
        elif (intent == 'print'):
            display(literals,variables,f)            
        elif (intent == 'while'):
            while_start(literals,variables,f)        
        elif (intent == 'stop'):
            while_stop(literals,variables,f) 
        else:
            print("\nIntent not available.") 
    #except:        
    #    print("Semantics Error")                

#%%
def initialize(literals,variables,f):
    l = len(variables)
    l1 = len(literals)    
    m = i = 0
    while m < looped:
        print("    ",end = '')
        f.write("    ")
        m += 1                
    if l1 !=0:
        if l == 0:
            while i<l1:
                var = variable_list.popleft()
                used_variables.append(var)
                s1 = str(literals[i])                
                print(var+' = '+s1)
                f.write(var+' = '+s1+"\n")                
                i = i + 1
        elif (l>l1):
               while i < l:
                   if (i != l1):
                       print(variables[i]+" = "+literals[i])
                       f.write(variables[i]+" = "+literals[i]+"\n")                       
                   elif (i >= l1 ):                       
                        print(variables[i]+" = "+literals[l1-1])
                        f.write(variables[i]+" = "+literals[l1-1]+"\n")                       
                   i += 1
        elif (l==l1):
            while i<l1:
                s1 = str(literals[i])                
                print(variables[i]+" = "+s1)
                f.write(variables[i]+" = "+s1+"\n")                
                i = i+ 1
        else:
            print("Check your logic please.")          
    else:          
        print(variables[1]+" = "+variables[0])
        f.write(variables[1]+" = "+variables[0]+"\n")    


#%%
def add(literals,variables,f):
    i=0
    l = len(variables)
    l_lit = len(literals)
    var = variable_list.popleft()
    result_variables.append(var)    
    k = 0
    while k < looped:
        print("    ",end = '')
        f.write("    ")
        k += 1                
    if ((l_lit == 1) and (l == 1)):    
        print(variables[0]+' = '+variables[0]+" + "+literals[0])
        f.write(variables[0]+' = '+variables[0]+" + "+literals[0]+'\n')   
    elif ((l==0) and (l_lit != 0)):        
        print(var+" = ",end='')
        f.write(var+" = ")        
        while i < (l_lit-1):
            print(literals[i]+' + ',end ='')
            f.write(literals[i]+' + ',)
            i += 1
        if (i == (l_lit-1)):
            print(literals[l_lit - 1])
            f.write(literals[l_lit - 1]+'\n')
    else:       
        print(var+" = ",end='')
        f.write(var+" = ")        
        while i < (l-1):
            print(variables[i]+" + ",end ='')
            f.write(variables[i]+" + ")             
            i = i+1
        if (i == l-1):
            print(variables[i])
            f.write(variables[i]+"\n")    
        

#%%
def subtract(literals,variables,f):    
    l = len(variables)
    l1 = len(literals)
    i=(l-1)
    j = (l1-1)    
    var = variable_list.popleft()
    result_variables.append(var)
    k = 0
    while k < looped:
        print("    ",end = '')
        f.write("    ")
        k += 1                
    if (l==1 and l1 ==1):        
        print(variables[0]+' = '+variables[0]+' - '+literals[0])
        f.write(variables[0]+' = '+variables[0]+' - '+literals[0]+'\n')        
    elif (l==0 and l1 !=0):    
        print(var+" = ",end='')
        f.write(var+" = ")        
        while j > 2:
            print(literals[j]+' - ',end ='')
            f.write(literals[j]+' - ',)
            j += 1
        if (j == 1):
            print(literals[j])
            f.write(literals[j]+'\n')
    else:        
        print(var+" = ",end='')
        f.write(var+" = ")       
        while i > 2 :
            print(variables[i]+" - ",end ='')
            f.write(variables[i]+" - ")
            i = i+1
        if (i == 1):
            print(variables[i])
            f.write(variables[i]+"\n")       


#%%
def multiply(literals,variables,f):
    i=0
    l = len(variables)
    l_lit = len(literals)
    var = variable_list.popleft()
    result_variables.append(var)    
    k = 0
    while k < looped:
        print("    ",end = '')
        f.write("    ")
        k += 1                
    if ((l_lit == 1) and (l == 1)):    
        print(variables[0]+' = '+variables[0]+" * "+literals[0])
        f.write(variables[0]+' = '+variables[0]+" * "+literals[0]+'\n')   
    elif ((l==0)and (l_lit != 0)):        
        print(var+" = ",end='')
        f.write(var+" = ")        
        while i < (l_lit-1):
            print(literals[i]+' * ',end ='')
            f.write(literals[i]+' * ',)
            i += 1
        if (i == (l_lit-1)):
            print(literals[l_lit - 1])
            f.write(literals[l_lit - 1]+'\n')
    else:       
        print(var+" = ",end='')
        f.write(var+" = ")        
        while i < (l-1):
            print(variables[i]+" * ",end ='')
            f.write(variables[i]+" * ")             
            i = i+1
        if (i == l-1):
            print(variables[i])
            f.write(variables[i]+"\n")    

    
#%%
def divide(literals,variables,f):
    i=0
    l = len(variables)
    l_lit = len(literals)
    var = variable_list.popleft()
    result_variables.append(var)    
    k = 0
    while k < looped:
        print("    ",end = '')
        f.write("    ")
        k += 1                
    if ((l_lit == 1) and (l == 1)):    
        print(variables[0]+' = '+variables[0]+" / "+literals[0])
        f.write(variables[0]+' = '+variables[0]+" / "+literals[0]+'\n')   
    elif ((l==0)and (l_lit != 0)):        
        print(var+" = ",end='')
        f.write(var+" = ")        
        while i < (l_lit-1):
            print(literals[i]+' / ',end ='')
            f.write(literals[i]+' / ',)
            i += 1
        if (i == (l_lit-1)):
            print(literals[l_lit - 1])
            f.write(literals[l_lit - 1]+'\n')
    else:       
        print(var+" = ",end='')
        f.write(var+" = ")        
        while i < (l-1):
            print(variables[i]+" / ",end ='')
            f.write(variables[i]+" / ")             
            i = i+1
        if (i == l-1):
            print(variables[i])
            f.write(variables[i]+"\n")    
    

#%%
def while_start(literals,variables,f):
    l = len(variables)
    s1 = str(literals[1])
    s2 = str(literals[0])
    k = m = 0
    while k < looped:
        print("    ",end = '')
        f.write("    ")
        k += 1                
    if l==0:
        var = variable_list.popleft()
        used_variables.append(var)
        temp.append(var)
        print(var+" = "+s2)
        f.write(var+" = "+s2+"\n")
        while m < looped:
            print("    ",end = '')
            f.write("    ")
            m += 1                   
        if (int(literals[1]) > int(literals[0])):
                print("while "+var+" < " +s1 +":")
                f.write("while "+var+" < " +s1 +":\n")               
        elif (int(literals[1]) < int(literals[0])):
            print("while "+var+" > " +s1 +":")
            f.write("while "+var+" > " +s1 +":"+"\n")              
        else:
            print("\nError 601")        
    else:
        var = variables[0]
        temp.append(var)
        print(var+" = "+s2)
        f.write(var+" = "+s2+"\n")        
        while m < looped:
            print("    ",end = '')
            f.write("    ")
            m += 1                   
        if (int(literals[1]) > int(literals[0])):
            print("while "+var+" < " +s1 +":")
            f.write("while "+var+" < " +s1 +":\n")  
        elif (int(literals[1]) < int(literals[0])):
            print("while "+var+" > " +s1 +":")
            f.write("while "+var+" > " +s1 +":\n")                            
        else:
            print("\nError 601")

def while_stop(literals,variables,f):    
    if (looped ==0):
        print("No loop is running.")    

#%%
def display(literals,variables,f):
    l = len(variables)
    l1 = len(result_variables)
    k = 0
    while k < looped:
        print("    ",end = '')
        f.write("    ")
        k += 1                
    if l == 0:
        print("print ("+result_variables[l1-1]+")")
        f.write("print ("+result_variables[l1-1]+")\n")     
    else:
        print("print ("+variables[0]+")")
        f.write("print ("+variables[0]+")\n")
    


#%%
#translator_input("initialize",[1,2],["X","Y"])
'''translator_input("initialize",[0],['Xsum'])
translator_input("while",['1','100'],["i",'100'])
translator_input("print",[7,8],['Xsum'])
translator_input("stop",[],[])

translator_input("initialize",[1,10],["A","Xsum"])
input("display",[1],[])
'''
#translator_input("subtract",['5'],['A'])
