#first way
list1=[1,43,12,89,64,23,56,77]

num=int(input("Enter the number you want to search in list"))

if num in list1:
    print("Element exits")
else:
    print("element do not exits")

    
    
#second way
list1=[1,43,12,89,64,23,56,77]

num=int(input("Enter the number you want to search in list"))
flag=0   
for i in list1:
    if i==num:
        flag=1
       
if flag==1:
     print("Element exits")
else:
    print("element do not exits")
