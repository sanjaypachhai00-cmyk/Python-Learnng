#JSON=JavaScript Object Notation  :is a universal format for exchnaging data between programs-(APIs,config. files)
{
    "name":"Sanaku",
    "age":"22",
    "topic":"nanochip"
}

#dictionary to json
import json
dict={
    "name":"Sanjay",
    "age":23,
    "topic":"ce",
    "class":"a",
    "salary":4000000000000
}
josn=json.dumps(dict)
print(josn)

#pretty printing
jnos=json.dumps(dict,indent=3)
print(jnos)


#json to dictionary
import json
TU="""{
    "Fruit ": "Apple",
    "Vegetable":"Cabbage",
    "Salad":"Carrot"
}"""
Json=json.loads(TU)
print(Json)

#write a json file
with open("TU.json","w") as file:
    json.dump(TU,file,indent=3)

#read
with open("TU.json","r")as file:
    TU=json.load(file)
print(TU)

# function	               Purpose
# json.dumps(obj)	           Python → JSON string
# json.loads(str)	           JSON string → Python
# json.dump(obj, file)	   Python → JSON file
# json.load(file)	           JSON file → Python