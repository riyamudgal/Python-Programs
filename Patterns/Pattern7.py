rows = int(input("Enter the number of rows: ")) 
for i in range(rows+1):  
    for j in range(i):  
        print(i, end=" ")    
    print()
    
    
'''
Output
Enter the number of rows: 6
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
6 6 6 6 6 6
'''
