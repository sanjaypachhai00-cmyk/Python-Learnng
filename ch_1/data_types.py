#data_type=kind of value a variable can Store 

             #interger

x=10
y=1_000_000
z=-10
print(type(z))
              #float
a=10.33
pi=3.14
print(type(pi))

                 #boolean

good=True
bad=False
print(type(good))

                     #complex
z=3+4j
print(z.real,z.imag)

                    #String(immutable)
name="sanjay"
GOAT="messi"

print(name[2:4])
print(len(GOAT))
print(name.upper())

#print(name[3])=e   (error as strings are immutable)
#
                          #LIST(ordered,mutable,duplication👍)

nums=[5,6,3,2,1]
print(nums)
print(nums.reverse())
nums.append(4)
print(nums)
nums.reverse()
print(nums)
nums.sort()
print(nums)


             #tuple(ordered,immutable)

n=(1,2,3,4)
            #n[0]=6❌(immutable)
print(n)


                   #set(unordered,unique)
a={1,3,5,3,2,1}
print(a)

a.add(9)
print(a)


                      #dict(immutable,key:value)

fruit={
    "Apple":"Sweet",
    "biteer_gourd":"bitter",
    "Lemon":"sour"

}
print(fruit)
print(fruit["Apple"])
#fruit["Apple"]=bitter(immutable)

              #none type
result=None
print(result)      
print(type(result))        

                #range(sequence)

for i in range(6):
    print(i)