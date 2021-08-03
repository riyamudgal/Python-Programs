rows=int(input("Enter the number of rows: "))  
for i in range(1,rows):  
    for j in range(1,i+1):    
        print(i*j, end='  ')  
    print()
    
    
'''Output
Enter the number of rows: 7
1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36
'''
