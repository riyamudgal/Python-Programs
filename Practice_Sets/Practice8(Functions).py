#using function find greatest among thre
def greatest(number1,number2,number3):
    if(number1>number2 and number1>number3):
        print(number1 ,"is greatest")
    elif(number2>number3):
            print(number2 ,"is greatest")
    else:
        print(number3 ,"is greatest")
number1=26
number2=14
number3=56
greatest(26,14,56)

#using function find greatest among thre with return
def greatest(number1,number2,number3):
    if(number1>number2 and number1>number3):
        return number1 
    elif(number2>number3):
            return number2 
    else:
        return number3 
#number1=12
#number2=65
#number3=42
great=greatest(12,65,42)
print( great, " is greatest. ")

#convert celsius to fahrenheit
def temperature(temp):
    return (temp*9/5)+32
c=int(input("Enter the Temperature in Celsius:  "))
f=temperature(c)
print("Temperature in Fahrenhite is : ", f)

# to print sum of 1st n natural numbers
def sum(n):
    if n==1 or n==0:
        return 1
    else:
        return n+sum(n-1)
n1=int(input("Enter the number : "))
n=sum(n1)
print(n)


#printing a pattern 
num=6
for i in range(num):
    print("*"*(num-i))

#inches into cms
def inch(i):
    return i*2.54
a=int(input("Enter the Value : "))
b=inch(a)
print (b)

#strip function
def replace(string, word):
    newstr=string.replace(word,"")
    return newstr.strip
name="my name is shrikant"
a=replace( name, "name")
print(a)
