#problem 1 store elements in a list enetered by user
f1=input("Enter fruit number 1 : ")
f2=input("Enter fruit number 2 : ")
f3=input("Enter fruit number 3 : ")
f4=input("Enter fruit number 4 : ")
f5=input("Enter fruit number 5 : ")
f6=input("Enter fruit number 6 : ")
f7=input("Enter fruit number 7 : ")

list=[f1,f2,f3,f4,f5,f6,f7]
print(list)


#marks of 6students and then sort them
m1=input("Enter marks of 1 student ->")
m2=input("Enter marks of 2 student ->")
m3=input("Enter marks of 3 student ->")
m4=input("Enter marks of 4 student ->")
m5=input("Enter marks of 5 student ->")

m6=input("Enter marks of 6 student ->")

marks=[m1,m2,m3,m4,m5,m6]
print(marks)
marks.sort()
print(marks)

#to sum a list with 4 numbers
numbers=[54,78,21,67]
#print(numbers[0]+numbers[1]+numbers[2]+numbers[3])
print(sum(numbers))                     #using predefined function

#count number of zeros
li=[2,5,9,0,0,2,3,4,5,0,0,0,7,6]
print(li.count(0))
