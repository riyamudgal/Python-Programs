#First Method, by creating function
def multiply(my_list):
    res=1
    for i in my_list:
        res=res*i
    return res
    
    
list1=[7,9,3,6,2,10]
list2=[9,6,8,7,0,4,6]

m_list1=multiply(list1)
m_list2=multiply(list2)

print(m_list1)
print(m_list2)


# second method ,using numpy.prod() from import numpy to get the multiplication of all the numbers in the list
import numpy
list1=[7,9,3,6,2,10]
list2=[9,6,8,7,0,4,6]
 

result1=numpy.prod(list1)
result2=numpy.prod(list2)

print(result1)
print(result2)




