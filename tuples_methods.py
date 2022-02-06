tuple=(23,76,11,65,23,89,11,67,43,87,54)
print(tuple)

#will return count of occurence of a particular element
count=tuple.count(23)
print(count)

#return the index of element
index=tuple.index(90)               #error because element is not present in the tuple
print(index)

index1=tuple.index(76)
print(index1)
