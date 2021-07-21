#smallest element

#sorting and then printing the 0 index element
list1=[89,23,56,12,75,34,18,70]
list1.sort()
print("Smallest element is ", list1[0])

#using min function
list1=[89,23,56,12,75,34,18,70]
print("Smallest element is:", min(list1))

#Find min list element on inputs provided by user
list1=[]
n=int(input("Enter the size of list"))
for i in range(n):
    element=int(input())
    list1.append(element)
print("Smallest element is ", min(list1))


#largest element
#sorting and then printing the 0 index element
list1=[89,23,56,12,75,34,18,70]
list1.sort()
print("Largest element is ", list1[len(list1)-1])

#using max function
list1=[89,23,56,12,75,34,18,70]
print("Largest element is:", max(list1))

#Find max list element on inputs provided by user
list1=[]
n=int(input("Enter the size of list"))
for i in range(n):
    element=int(input())
    list1.append(element)
print("largest element is ", max(list1))

#second largest element
list1 = [89,23,56,12,75,34,18,70]
list1.sort()
print("Second largest element is ", list1[-2])
