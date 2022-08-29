#!/usr/bin/env python
# coding: utf-8

# # This Is Python Tutorial

# this is our first program in python: it just started here

# In[1]:


print("Hello world")


# 
# Variables

# # VARIABLES

# In[3]:


x = 3


# In[4]:


get_ipython().run_line_magic('whos', '')


# In[2]:


a,b,c,d,e,f = 4,5.8,9,2,7,-3


# In[3]:


get_ipython().run_line_magic('whos', '')


# # OPERATORS

# In[4]:


sumOfaAndb = a+b


# In[5]:


print(sumOfaAndb)


# # BOOL

# In[6]:


a = True
b = True
c = False


# In[7]:


print (a and b)
print (a and c)
print (c and a)


# In[8]:


d = a or c
print(d)


# In[9]:


not(a)


# In[10]:


not(b)


# In[11]:


not(c)


# In[12]:


t = not(d)


# In[13]:


type(t)


# # comparisons

# In[14]:


print(2<3)


# In[15]:


c = 2<3
print(type(c))
print(c)


# In[16]:


d = 3==4


# In[17]:


print(d)


# In[18]:


3==3.0


# In[19]:


x = 4
y = 9
z = 8.3
r = -3


# In[20]:


(x<y) and (z<y) or (r==x)


# # ROUND function

# print(round(4.556))

# In[22]:


print(round(4.345))


# # isinstance function

# In[23]:


isinstance(3,int)


# In[25]:


isinstance(3.4,(float,int))


# In[27]:


isinstance(2+3j,(int,float))


# # power function

# In[28]:


pow(2,4)


# In[29]:


2**4


# In[30]:


pow(2,4,7)


# # INPUT FUNCTION 

# In[31]:


x = input("Enter a number :")


# In[32]:


type(x)


# In[33]:


x = int(x)


# In[34]:


type(x)


# In[35]:


print(x-34)


# In[36]:


a = float(input("Enter a real number :"))


# In[37]:


type(a)


# # CONTROL FLOW (if condition)

# In[1]:


a = int(input())
b = int(input())
if a>b:
    print(a)
    print("I am still inside if condition")
print("I am outside if condition")    


# In[2]:


a = int(input())
b = int(input())
if a>b:
    print(a)
if b>a:
    print(b)


# # CONTROL FLOW (if-else)

# In[7]:


a = int(input())
b = int(input())
if a>b:
    print(a)
    print("if part")
else:
    print(b)
    print("else part")


# # CONTROL FLOW (if-elif-else)

# In[8]:


a = 1
b = 5
if a==b:
    print("Equal")
elif a>b:
    print("A")
else:
    print("B")
print("Not in if")


# In[14]:


a = int(input("Enter Marks:"))
if a >= 85:
    print("A Grade")
elif (a < 85) and (a >= 80):
    print("A- Grade")
elif a < 80 and a >= 75:
    print("B Grade")
elif a < 75 and a >= 70:
    print("B Grade")
else:
    print("Below Average")


# In[15]:


a = 3 
if a>10:
    print(">10")
elif not(a>10):
    print("Else part")


# # CONTROL FLOW (Nested if)

# In[16]:


a = int(input())
if a>10:
    print(">10")
    print("Inside the top if")
    if a>20:
        print(">20")
        print("inside the nested if")
    else:
        print("<=20")    
        print("Inside the else part of nestrd if")
print("Outside all ifs")


# # CONTROL FLOW (Loops)

# In[ ]:


# single line comment
"""
User will enter a floating point number let say 238.915. Your task
is to find out the integer portion before the pooint (in this case 238)
and then check if that integer portion is an even number or not?
"""
x = float(input("Enter a real number :"))
y = round(x) 
if y>x:
    intPortion = y-1 # 29.6
else:
    intPortion = y
print(intPortion)


# In[1]:


n = int(input())
i = 1
while i < n:
    print(i**2)
    print("thist is interation number :", i)
    i+=1
print("Loop done")
    
    


# In[4]:



n = 10
i = 1
while True:
    if i%9 == 0:
        print("inside if")
        break
    else:
        print("inside else")
        i = i+1 # i+=1
print("done")


# In[1]:


n = 10
i = 1
while True:
    if i%9 != 0:
        print("inside if")
        i +=1
        continue
    print("something")
    print("somethingelse")
    break
    
print("done")


# # FOR LOOP

# In[4]:


L = []
for i in range(0,10,2):
    print(i)
    L.append(i**2)
print(L)


# # ELSE IN FOR LOOPS

# In[2]:


S = {"apple",4.9,"cherry"}
i = 1
for x in S:
    print(x)
    i+=1
    if i==3:
        break
    else:
        pass
else:
    print("loop terminates with success")
print("outside the loop")


# # CONTROL FLOW(EXPLORING A DICTIONARY)

# In[4]:


d = {"a":10, "b":-19,"c":"abc"}
for x in d:
    print(x,d[x])


# In[5]:


""" given a list of numbers i.e [1,2,3,4,-5,7,9,3,2], make another list that
contains all the items in sorted order from min to max. i.e your result
will be another list like [-5,1,2,2,3,3,7,9]
"""
L = [1,2,4,-5,7,9,3,2]

m = L[0]
for i in L:
    if i<m:
        m = i
print(m)


# # FUNCTIONS

# In[2]:


def printsucces():
    print("i am done")
    print("send me another task")


# In[4]:


printsucces()


# In[5]:


23+6


# In[6]:


def printsucces2(): # doc string
    """ this function is doing nothing except printing a message.
    that message is "hello"
    """
    print("hello")


# In[7]:


get_ipython().run_line_magic('pinfo', 'printsucces2')


# In[8]:


printsucces2()


# In[16]:


def printMsg(msg): # input arguments
    """ the function prints the message supplied by the user or 
    prints that msg is not in the form of string"""

    if isinstance(msg,str):
        print(msg)
    else:
        print("Your input argument is not string")
        print("here is type of what you have supplied :",type(msg))
            


# In[1]:


def mypow(a,b):
    """ this function computes power just like bultin pow function"""
    c = a**b
    print(c)


# In[2]:


get_ipython().run_line_magic('pinfo', 'mypow')


# In[3]:


mypow(3,4)


# In[9]:


def checkArgs(a,b,c,):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
         print((a+b+c)**2)
    else:
         print("error: the input arguements are not of expected type")


# In[10]:


checkArgs(3,4,5)


# In[12]:


checkArgs(4,5,"g")


# In[13]:


def f(a,b,c): # order of input arguments
       print("A is :",a)
       print("B is :",b)
       print("C is :",c)


# In[14]:


f(2,3,"game")


# In[15]:


f(a = 4, b = 5, c ="game")


# In[17]:


def myadd(a,b):
    sumvalue = a+b
    return sumvalue                   # return statement


# In[18]:


d = myadd(3,2)
print(d)


# In[19]:


variableoutsidethefunction = 3


# In[20]:


def g():
    print(variableoutsidethefunction)


# In[21]:


g()


# In[1]:


def myadduniversal(*args): # variable number of input arguments
       s = 0
       for i in range(len(args)):
           s += args[i] # s = s+args[i]
       return s


# In[4]:


print(myadduniversal(2,4,5,4.6,78))


# In[5]:


def printallvariablenamesandvalues(**args):
    for x in args:
        print("variable name is :",x,"and value is :",args[x])
        


# In[6]:


printallvariablenamesandvalues(a = 3,b = "B",c = "CCC",y =6.7)


# In[7]:


def gg(s=4): # default values
    print(s)


# In[8]:


gg()


# In[9]:


L =[1,2,3]
L2 = L
L2[0] = -9
print(L)


# In[10]:


def ff(L=[1,2]):
    for i in L:
        print(i)


# In[11]:


L2 = [12,3,4]
ff()


# In[12]:


ff(L2)


# # Modules

# In[56]:


import sys
sys.path.append('//Users/djlazer/phy/')


# In[57]:


import my_universal_functions as myfs


# In[55]:


get_ipython().run_line_magic('pinfo2', 'myfs.addallnumerics')


# In[39]:


c = myfs.addallnumerics(2,3,4,6)


# In[40]:


print(c)


# In[12]:


myfs.myname


# # STRING

# In[1]:


S = "python"
T = 'its a good data science language'


# In[3]:


print(T)


# In[4]:


type(T)


# In[6]:


print('Hello',12,'Hello2',"Who are you",5.9)


# In[7]:


price = 12 
s = "The price of this book"
v = s + ' is: ' + str(price)
print(v)


# In[9]:


# Multi line string
a = """this is line 1
this is line 2
this is last line and this is 3"""
print(a)


# In[10]:


print(""" the following options are available:
                     -a        : does nothing
                     -b.       : also does nothing
""")


# In[11]:


# string indexing and slicing
s = "how are you ? and who are you ?"
print(s[5])


# In[12]:


s[0:13]


# In[13]:


s[-18:-5]


# In[14]:


s[0:13:3]


# In[15]:


s[0:]


# In[16]:


# strip
a = "    abc def    hgh srdghfj   "
b = a.strip()
print(b)


# In[20]:


#lower case
a = "ABE DRK ;; zxcvbnm Dddff"
b = a.lower()
print(b)


# In[21]:


# upper case
c = a.upper()
print(c)


# In[22]:


# replace
d = a.replace(";","*")
print(d)


# In[23]:


d = a.replace(";","**&&^^%%")
print(d)


# In[24]:


d = a.replace(";;","two semi colons")
print(d)


# In[25]:


# split
a = "abc;def;hghytio;yy23"
L = a.split(";")
print(L)


# In[28]:


print("we are learing \"string\" here")


# In[29]:


print('we are learing "string" here')


# In[31]:


print(r"c:\name\drive")


# In[ ]:




