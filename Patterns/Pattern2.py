#printing pattern
n=int(input("Enter the number of lines"))
for i in range(n+1):
    print("*" *i)
    
    
'''Output:
Enter the number of lines 5
 *
 **
 ***
 ****
 *****
 '''

for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end="")
    print("\n")
    
    
'''Output
*

**

***

****

*****
'''
