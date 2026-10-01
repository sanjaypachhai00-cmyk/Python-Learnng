#1) for(list,string,range...)

fruits = ["apple", "banana", "mango"]  #LIST

for fruit in fruits:
    print(fruit)


for ch in "Python":    #STRING
    print(ch)


for i in range(9):  #RANGE(start,stop,step)
    print(i)

for ch in "congratulations":
    print(ch)

for i in range(10,100,10):
    print(i)




#2)Repeats as long as the conditions is true

a=1
while a<=5:
    print(a)
    a += 1

#Q keep asking until user enters a valid password
username=" "

while username != "groot":
    username=input("Enter the username:")
print("Access Granted")


#3)break
for i in range (1,12):
    if i==4:
        break
    print(i)


#4 to search a number in a list
num=[1,2,3,4,5,6,7,8,9]
m=int(input("Enter a number to search in a list"))
for n in num:
    if n==m:
        print(f"{m} is in the list")
        break
    else:
        print("Number not found")


#5 continue
for i in range(1,10):
    if i==4:
        continue
    print(i)

    #q print only odd numbers
for i in range(1,20):
    if(i%2==0):
        continue
    print(i)

    #q multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()      # newline after each row

#q pattern

for i in range(1,  11):
    print("*" * i)


for i in range(1,6):
    for j in range(1,11):
        print("*"*(i*j))



#SUM
n=int(input("Enter a number"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

#factorial
m=int(input("ENter a number"))
fact=1
for i in range(1,m+1):
    fact=fact*i
print(fact)

#reverse
y=int(input("Enter a number to reverse:"))
rev=0
while y>0:
    last_digit=y%10
    rev=rev*10+last_digit
    y=y//10
print(rev)