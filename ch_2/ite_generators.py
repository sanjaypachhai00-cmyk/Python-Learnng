#ITERATORS; any object we can loop with for.

# for x in [1, 2, 3]:       # list → iterable
# for c in "hello":          # string → iterable
# for k in {"a": 1}:         # dict → iterable
# for i in range(5):         # range → iterable
# for line in open("f.txt"): # file → iterable

for x in [1,2,3,4]:
    print(x)

#This is simply
it=iter([1,2,3,4])
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break


#GENERATOR:simple way of making the iterator(yeild)
def numbers():
    for i in range(1, 1000001):
        yield i
        print(i)

#return: exits the function
#yeild:stops the function,remember state and resumes on the next call

def simple():
    print("Start")
    yield 1

    print("Processing")
    yield 2

    print("Stop")
    yield 3
g=simple()
print(next(g))
print(next(g))
print(next(g))
#The generator doesn't compute everything at once — it produces values on demand.

#generatoer expressions

square=[x*x for x in range(5)]
print(square)
print(list(square))

#wih built in functions

total=sum(x*x for x in range(100))
print(total)

total1=any(x%7==0 for x in range(1,100))
print(total1)

#INFINITE GENERATOR
#FIBONACCI GENERATOR
