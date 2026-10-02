# #OOP: is a programming paradaigm in which code is organized into objects that combine data and behaviour

# #CLASS: blueprint of a car
# #OBJECT: an actual object built from a car


# #example
# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def bark(self):
#         print(f"{self.name} barks woof!")

# d1=Dog("max",12)
# d2=Dog("Tommy",1)
# print(d1.name)
# d1.bark()



# #_inti_ method(constructor)

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s=Student("Samir",63)
# print(s.name,s.age)
# print(s.age)



# #class attribute
# class Ram:
#     college="XYZ_engineering"

#     def __init__(self,name):
#         self.name=name
# r=Ram("Sita")
# print(r.college)
# print(r.name)

# #static method(no self or cls)
# class Math:
#     @staticmethod
#     def add(a,b):
#         return(a+b)
# print(Math.add(2,3))


# #Dunner/magic method(python calls it automatically)
# class Mango:
#     def __init__(self,taste):
#         self.taste=taste
#     def __str__(self):                              #__str__ is a special method
#         return f"Fruit is  {self.taste}"
# m=Mango("Sweet")
# print(m)

# #__repr__   __eq__  __len__   __add__

# #ENCAPSULATION(data hiding)
# #self.name = "Aarav" (public)
# #self._age = 20    # "Don't touch unless you know what you're doing"   -=single underscore:protected
# #self.__age = 20    # "Don't touch unless you know what you're doing"      =private



#INHERITANCE
class Animal:
    def __init__(self,name,legs):
        self.name=name
        self.legs=legs
    def eat(self):
       print ( f"{self.name} is eating")
class dog(Animal):                                 #inhertance
    def sound(self):
        print( f"{self.name} is barking")
d=dog("MAX",4)
d.eat()
d.sound()

#single,multiple,multilevel,isinstance(),issubclass()


#Overriding methods

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

Dog().sound()   # Woof!
Cat().sound()   # Meow!


#POLYMORPHISM(different class-same method-different way of impl.)
class Dog:
    def sound(self):
        print("Woof")

class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

for animal in [Dog(), Cat(), Cow()]:
    animal.sound()


#Abstraction
from abc import ABC ,abstractmethod
class Laptop(ABC):
    @abstractmethod
    def start(self):
        pass
class Mobile(Laptop):
    def __init__(self,price):
        self.price=price    

    def start(self):
        return f"{self.price} is high"
m=Mobile(34000)
print(m.start())

