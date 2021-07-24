list1=[[1,2],[6,4],[4,9],[6,2]]
list2=[[1,2],[2,4],[4,9],[0,5]]

new_list=[]
for i in list1:
    if i not in list2:
        new_list.append(i)
        
for i in list2:
    if i not in list1:
        new_list.append(i)
        
        
print(new_list)
