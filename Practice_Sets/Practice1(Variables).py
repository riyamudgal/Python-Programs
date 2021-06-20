#sum of two numbbers
c=12
d=89
ans=c+d
print(ans)


a=10
b=90
print("Sum of 10 and 90 is ->", a+b)

#finding remainder 
a=24
b=10
rem=a%b
print("Remainder when 24 is divided by 10 -> ",rem)

#type of variable entered in input()
var=input("Enter any thing ->")
print(type(var))
v=int(var)
print(type(v))

#compare two numbers
a=16
b=90
c=a>b
print(c) 

#average of numbers input by  user
var=int(input("Enter number 1-> "))
var2=int(input("Enter number 2-> "))
var3=int(input("Enter number 3-> "))
avg=(var+var2+var3)/3                    #answer will be in float datatype
print("Average of numbers is ->", avg)
avg=(var+var2+var3)//3                    #answer will be in int datatype
print("Average of numbers is ->", avg)


#square of a number
a=int(input("The square of the number is:"))
print(a*a)
