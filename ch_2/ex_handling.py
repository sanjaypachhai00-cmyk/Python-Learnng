#exception_handling:way of handling errors while a program is running
# n=int(input("Enter a number"))
# print(10/n)  #if 0 is input number then it gives:ZeroDivisionError

#try ans except

try:
    n=int(input("Enter a number"))
    print(10/n) 
except:
    print("Something went wrong")


#finally
try:
    x=int(input("Enter a number"))
except:
    print("Something went wrong")
finally:
    print("Code Executed sucessfully")

#example
try:
    num=int(input("Enter a number"))
    res=(100/num)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Division by zero not allowed")
else:
    print(res)
finally:
    print("Code Executed successfully")