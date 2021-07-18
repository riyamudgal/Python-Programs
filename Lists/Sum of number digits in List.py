list1=[32,76,19,63,29,55,90]

print("Original List is \n ", list1)

new_list=[]
for i in list1:
    sum=0
    for j in str(i):
        sum=sum+int(j)
    new_list.append(sum)
        
print("New list is \n ", str(new_list))

'''Output

Original List is 
  [32, 76, 19, 63, 29, 55, 90]
New list is
  [5, 13, 10, 9, 11, 10, 9]
  '''
