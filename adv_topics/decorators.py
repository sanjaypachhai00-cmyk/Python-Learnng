#DECORATORS   :function that takes another function as argument and returns the function

#SYNTAX
def decorators(func):
    def wrapper():
        print("Transaction initialized")
        func()
        print("Transaction completed")

    return wrapper()


#eg.                          :without decorator
def greet():
    print("Starting...")
    print("Hello Sanjay")
    print("Finished!")

@decorators                #  :with decorator
def hello():  
    print("Hello susmita" )                                      #Transaction initialized
                                                                 #Hello susmita
                                                                 #Transaction completed



def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper
@decorator
def greet():
    print("Hello Sanjay")
greet()



def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is running")
        result = func(*args, **kwargs)
        print("Function completed")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b
result = add(10, 20)
print(result)