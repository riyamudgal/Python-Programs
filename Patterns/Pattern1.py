#printing a pattern
n=int(input("Enter the number of rows: "))
for i in range(n):
    print(" " *(n-i-1), end=" ")
    print("*"*(2*i+1),end=" ")
    print(" " * (n-i-1))
    
    
'''Output
Enter the number of rows:
     *  
    ***
   *****
  *******
 *********
 
'''
