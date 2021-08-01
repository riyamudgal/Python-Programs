rows=int(input("Enter the number of rows: "))  
for i in range(1,rows + 1):  
    for j in range(1,rows + 1):  
        if j<=i:  
            print(i,end=' ')  
        else:  
            print(j,end=' ')  
    print()   
    
    
    
'''
Output
Enter the number of rows: 6
1 2 3 4 5 6
2 2 3 4 5 6
3 3 3 4 5 6
4 4 4 4 5 6
5 5 5 5 5 6
6 6 6 6 6 6
'''
