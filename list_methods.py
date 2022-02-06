list=[2,5,3,8,15,29,17,26,1]
print(list)

#sorting
list.sort()
print(list)

#reverse
list.reverse()
print(list)

#append
list.append(21)
print(list)

#insert
list.insert(4,16)
print(list)

# #above all methods works on previously updated list, just above that particular function

#pop
var=list.pop(5)
print(list)
print("Popped element is -> ", var)                #because popped element returns the value popped that's why we have stored it in a variable

#remove
list.remove(16)
print(list)
