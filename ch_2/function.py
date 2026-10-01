#function=reusable block of code
def greet(name):
    print(f" hello {name}")
greet("ram")
greet("hari")


#multiple parameters
def add(a,b):
    print(a+b)
add(2,3)


#return
def mul(x,y):
    return x*y
print(mul(3,4))

#lambda
square=lambda x:x**2
print(square(5))

add = lambda h,i:h+i
print(add(2,3))
