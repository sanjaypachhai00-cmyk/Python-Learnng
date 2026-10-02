#COMPREHENSIONS: simple and clean way to create a collection

#1)LIST  -ordered,mutable(unchangable)and allow duplicates
num=[1,2,3,6,7,2,3]
print(num)

# Adding items
# append(x)	:Add one item to end
# extend(iterable)	:Add all items from another iterable
# insert(i, x)	:Insert at index i

# python
# nums.append(10)          # [3,1,4,1,5,9,2,6,10]
# nums.extend([7, 8])      # adds 7, 8
# nums.insert(0, 100)      # insert 100 at index 0

# Removing items
# remove(x)	Remove first occurrence of value x
# pop(i)	Remove & return item at index i (default last)
# clear()	Remove all items
# del lst[i]	Delete item at index
# del lst[1:3]	Delete a slice

# python
# nums.remove(1)      # removes first 1
# x = nums.pop()      # removes last item, returns it 
# y = nums.pop(0)     # removes first item
# nums.clear()        # empties list
num.remove(2)
print(num)
#num.clear()
print(num)
print("Length:")
print(len(num))
print(sum(num))

#example
sq=[i*i for i in range(12)]
print(sq)
multiply=[x*2 for x in range(12)]
print(multiply)

#SET                                unordered,unique element only
sqq={i*i for i in range(10)}
print(sqq)
s={1,2,3,4,5}
s.add(9)
print(s)
s.remove(1)
print(s)


#SET OPERATIONS
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b        # union         → {1,2,3,4,5,6}
a & b        # intersection  → {3, 4}
a - b        # difference    → {1, 2}
a ^ b        # symmetric diff→ {1, 2, 5, 6}

# Same with methods:
a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)


#DICTIONARY
squares={x:x*x for x in range(11)}
print(squares)

name=["leo","messi","hari","ram"]
age=[12,45,64,21]


eff={name:age for name,age in zip(name,age)}
print(eff)
x={x:x*x for x in num if x%2==0}
print(x)