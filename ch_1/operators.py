                      #OPERTATORS(symblos that perform operations)

#1)Arithmetic Operators
a=64
b=32
print(a+b)
print(a-b)
print(a*b)
print(a//a)
print(b%a)
print(a%b)

#2)Comparison/Relational

print(a==b)
print(a!=b)
print(a<b)

#3)Logical
print("LOGICAL")
print(a==b and a<=b)  #and
print(a!=b or a>b)    #or
print(not a<b)      #not


#3)Assignment
a=3
a+=3
print(a)
a-=3
print(a)

#4)Bitwise(binary and ,or,xor,nor,left shift,right shift)

print(5&3)
print(5|3)
print(5^3)
print(5<<3)
print(5>>3)

#4)Membership

fruit=["apple","mango","cherry"]
print("apple" in fruit)
print("strawberry" not in fruit)


#QUESTIONS
#Q)Input two numbers and check if they are even or odd.
x,y=map(int,input("Enter two numbers").split())
if (x%2==0 and y%2==0):
    print(f"{x} , {y} are even number")
else:
    print(f"{x} , {y} are odd number")
