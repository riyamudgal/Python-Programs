#using list comprehensions

list1 = [10,21,4,78,32,97,67,39,45,66,93]
even_nums= [num for num in list1 if num%2==0]
print("Even numbers in the list: ", even_nums)

odd_nums= [num for num in list1 if num%2!=0]
print("Odd numbers in the list: ", odd_nums)


#lambda expression
list1 = [10,21,4,78,32,97,67,39,45,66,93] 
even_nums=list(filter(lambda x: (x%2==0), list1))
print("Even numbers in the list: ", even_nums) 

odd_nums=list(filter(lambda x: (x%2!=0), list1))
print("Odd numbers in the list: ", odd_nums)
