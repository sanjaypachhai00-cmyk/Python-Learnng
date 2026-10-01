#OOP: is a programming paradaigm in which code is organized into objects that combine data and behaviour

#CLASS: blueprint of a car
#OBJECT: an actual object built from a car

#example
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(f"{self.name} barks woof!")

d1=Dog("max",12)
d2=Dog("Tommy",1)
print(d1.name)
d1.bark()

#_inti_ method(constructor)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s=Student("Samir",63)
print(s.name,s.age)