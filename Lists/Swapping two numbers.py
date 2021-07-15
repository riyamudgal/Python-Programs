def swapping(list1, pos1,pos2):
    temp=list1[pos1]
    list1[pos1]=list1[pos2]
    list1[pos2]=temp
    
    return list1
    
list1=[1,2,3,4,5,6,7,8]
print("Before swapping list is -> \n")
pos1=int(input("Enter first position"))
pos2=int(input("Enter second position"))

newlist=swapping(list1,pos1,pos2)
print("After swapping new list is -> \n")
print(newlist)
