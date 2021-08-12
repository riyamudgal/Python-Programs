def no_duplicates(l):
    new_list = []
    [new_list.append(x) for x in l if x not in new_list]
    return new_list

list1=input("Enter the string")
list1=' '.join(no_duplicates(list1.split()))
print(list1)

'''
Output
Enter the string hey How are Jack Hope Sam you are good Jack  
hey How are Jack Hope Sam you good
