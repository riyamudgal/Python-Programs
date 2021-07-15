def Copying(list1):
    list_copy = list1[:]            #using slicing operator
    return list_copy
  
# Driver Code
list1 = [23,76,17,90,43,71,55]
list2 = Copying(list1)
print("Original List:", list1)
print("After Cloning:", list2)


#copying using extend()
#This appends each element of the iterable object to the end of the new list.

def Cloning(list1):
    list_copy = []
    list_copy.extend(list1)
    return list_copy
  
# Driver Code
list1=[23,76,17,90,43,71,55]
list2 = Cloning(list1)
print("Original List:", list1)
print("After Cloning:", list2)

