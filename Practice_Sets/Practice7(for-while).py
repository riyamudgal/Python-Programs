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
        
#printing sum of first n natural numbers using formula
num=int(input("Enter the value of num"))
sum=0
while num>0:
    sum+=num          #sum=sum+num
    num-=1            #num=num-1
print(sum)


#using for loop
a=int(input("Enter the number"))
sum=0
for s in range(1,a+1):
    sum+=s
    s=s+1
print(sum)

#factorial of a number using for loop
a=int(input("Enter the number: "))
fact=1
for i in range(1,a+1):
    fact*=i
print("The factorial of " ,a, "is: ", fact)

#using while while loop
a=int(input("Enter the Number: "))
fact=1
while a>0:
    fact*=a
    a-=1
print("The factorial of number is: ", fact)


#using factorial function
num=int(input("Enter any number ->"))
print("Factorial of ", num ,"is ->", math.factorial(num))
