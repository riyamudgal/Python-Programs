A={2,4,6,12,34,39,12}
print(type(A))
print (A)                  #repition is not allowed

A={}
print(type(A))             #empty set is treated as a dictionary

#emptty set can be created using below syntax
emptyset=set()
print(type(emptyset))

#adding elements
emptyset.add(76)
emptyset.add(61)
emptyset.add(69)
emptyset.add(90)
print(emptyset)

#calculating length
set={2,4,6,12,34,39,12}
print(len(set))                  #will not count the duplicate

#removing element from set
set.remove(6)
print(set)

#pop
set.pop()
print(set)

#again pop
set.pop()
print(set)

#clear set
set.clear()
print(set)

#union the sets
B={45,34,12,2,32}
print(B.union({3,99}))

#intersection of 2 sets
print(B.intersection({45,12,2}))

