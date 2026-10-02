#LAMBDA(anonymous function)     short and simple
square=lambda x:x*x
print(square(5))

add=lambda a,b:a+b
print(add(2,3))

#no arguements
n=lambda:42
print()

#conditionals
e_o=lambda a:"even" if a%2==0 else "odd"
print(e_o(6))


#MAP(applies a function to every item in iterable)
n=[5,3,8,9,22,4]
sq=list(map(lambda x:x*x,n))
print(sq)
print(type(sq))

#FILTERS :used to select items that satisfy the condition
p=[77,6,54,3,2,90]
even=filter(lambda x:x%2==0,p)
print(list(even))

#keep long words
words=["sameer","samir","ayoush","susmita","manish","dipesh","sandesh","rohit"]
six=filter(lambda word: len(word)>5,words)
print(list(words))
print(list(six))

#print positive number
o=[-1,0,-3,4,5,9]
positive=list(filter(lambda x:x>0,o))
print(list(positive))


#REDUCE :reduce multiple values to one value
from functools import reduce
numb=[1,2,3,4,5,6,7]
result=reduce(lambda f,g:f+g,numb)              #for addition
print(numb)
print(result)
result1=reduce(lambda s,d:s*d,numb)            #for multiplication
print(result1)





