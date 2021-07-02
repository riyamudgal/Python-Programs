a=[3,6,8,14,19]
print(a)
print(a[0])
print(a[1])

#List can have heterogenous elements
#name= ["Saksham",20,19//08//2002,"Bulandshahr"]
name1= ["Saksham",20,"19 august 2002","Bulandshahr",120000.00,True]
print(name1)
print(name1[2])
name1[3]='Ghaziabad'
print(name1)

#list slicing
print(name1[:3])
print(name1[-4:])                 #negative indexing is done from end, starting from 0 but we begin with -1 and end to -n

#to calculate length
print(len(name1))
