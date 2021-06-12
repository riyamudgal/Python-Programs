#printing table
num=int(input("enter any number"))
i=1
while i<=10:
    print(num," * ",i," = ",i*num)
    i=i+1

#printing table using for loop
num=int(input("enter any number"))
i=1
for i in range(1,11):
    print(num," * ",i," = ",i*num)
    i=i+1

#printing the name start with particular alphabet
L1=["harry","sohan","sachin","rahul"]
for name in L1:
    if name.startswith("s"):
        print("hello "+ name)

#checking wether a number is prime or not
num=int(input("enter any number"))
temp=False
for n in range(2,num):
    if(num%n==0):
        temp=True
        break
if temp:
        print("it is a prime number")
else:
        print("it is not a prime number")
