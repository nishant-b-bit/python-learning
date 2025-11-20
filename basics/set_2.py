#set methods 

name={"nishant",1,2,2,2,"budha"}
print(name.pop())#pyhton will pop the random element from the set
print(name.pop())
print(name.pop())
name.clear()# will make the set empty
print(name)

set1={1,2,3}
set2={1,2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))