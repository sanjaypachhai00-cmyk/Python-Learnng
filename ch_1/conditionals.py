#conditionals(make decision based on conditions)

#1) IF
age=20
if(age>18):
    print("You can vote")
print("Did you vote")

#2 ELSE
if(age>18):
    print("VOte")
else:
    print("No vote")

#3) if/elif/else
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")

#4) if/else/and
username=input("ENter the username")
password=input("ENter the password")
if username=="LEO" and password=="groot":
    print("User verified")
else:
    print("Invalid user")

#5)
a,b,c=map(int,input("Enter three numbers").split())
if(a>b and a>c):
    print(f"{a} is greatest")
elif(b<a and b>c):
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")
