#TYPE HINTS
                 #NORMAL
name="sujata"
age=23

                    #TYPE HINT
name: str="Sanjay"
age: int="34"
print(age)

# Common type hints

# Type          Hint       	Example
# String	    str	       "Hello"
# Integer	    int	        25
# Float	        float	    10.5
# Boolean	    bool	    True
# List	        list	    [1, 2, 3]
# Dictionary	dict	    {"name": "Sanjay"}
# Tuple	        tuple	    (10, 20)
# Set	        set	        {1, 2, 3}

#normal
def add(a,b):
    return(a,b)

#type hint
def add(a:int,b:int)->int:
    return a+b
print(add("Hello", "World"))    #Type hint donot force the type


#For variables
name:str="sanjay"
age:int=23
height:float=8.4
is_There:bool=True

name:str
fruit:str
length:float


#Type hint for list
names: list[str] = ["Sanjay", "Ram", "Hari"]
fruit:list[int]=[1,2,3,4,5,6,7,8,9,67,34,56]

#Type hint for dictionary
student:dict[str,int]={
    "name":"susmita",
    "age":23,
    "position":1
}

# So type hints improve:

# Readability
# Code documentation
# IDE support
# Error detection
# Maintainability
# Large-project development

def calculate_average(marks: list[float]) -> float:
    total: float = sum(marks)
    average: float = total / len(marks)
    return average


marks: list[float] = [80.5, 75.0, 90.5]

result: float = calculate_average(marks)

print(result)