x=0
y=1
num=int(input("Enter the number upto which you want to find fibonacci series"))
print(f"fibonacci Series upto {num} is")                     #using f string
while y<num:
    print(y)
    x = y
    y = x+y
    
    
#can also be written as

x,y=0,1
num=int(input("Enter the number upto which you want to find fibonacci series"))
print(f"Fibonacci Series upto {num} is")
while y<num:
    print(y)
    x,y = y,x+y
    
    
'''
Output
Enter the number upto which you want to find fibonacci series23
Fibonacci Series upto 23 is
1
1
2
3
5
8
13
21
'''


