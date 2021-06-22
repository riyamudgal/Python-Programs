#factorial of a number
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)

n=int(input("Enter any number -> "))
fact=factorial(n)
print(fact)
