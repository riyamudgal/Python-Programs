#using Counter(), finding occurrence of particular element

from collections import Counter
 
l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
 
x = 3
d = Counter(l)
print(f"{x} has occurred {d[x]} times")

#using Counter(), finding occurrence of all the elements
from collections import Counter

l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
 
d = Counter(l)
print(f"occurrence of all ellements is \n {d} ")


