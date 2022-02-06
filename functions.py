def percentage(marks):
    return ((marks[0]+marks[1]+marks[2]+marks[3]+marks[4])/400)*100

marks1=[65,76,86,54,58]
percentage1=percentage(marks1)

marks2=[45,65,57,73,67]
percentage2=percentage(marks2)

marks3=[45,48,56,63,78]
percentage3=percentage(marks3)
print(percentage1 , percentage2 , percentage3)


def surname(name):
    print("Good Evening", name)

surname("Saksham Mudgal")

#function with arguments and return
def subtraction(n1, n2):
    return n1-n2
N=subtraction(38,23)
print(N )


#Taking inputs for function
def multiplication(N1,N2):
    return N1*N2
Num1=int(input("enter 1st number: "))
Num2=int(input("enter 2nd number: "))
Multi=multiplication(Num1,Num2)
print(Multi)


#fefault parameter value
def function(val1=1, val2=1):
    ans=val1+val2
    print("Sum of two numbers is -> ", ans)

function(12,12)


