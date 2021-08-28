string="python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
s=len(string))    #length of string
print(f"Length of string is ->{s}")
'''Output
Length of string is ->327'''


#string ends with
print(string.endswith("Happy"))                    #endswith() method returns True if the string ends with the specified value, otherwise False.


#to find occurence
print("Occurrence of particular alphabet->")
print(string.count("p"))
'''
Output
Occurrence of particular alphabet->13
'''


#to capitalize                              #will capitalize first character of the string
print(string.capitalize())



#to find a string
print("Python is found at ->")
print(string.find("Python"))
'''
Output
Python is found at ->74
'''


#to replace a string
print("After replacement new string is->")
print(string.replace("Python's","java"))              #first one: to replace, second: to be replaced by
'''Output
After replacement new string is-> python is an interpreted high-level general-purpose programming language. java design philosophy emphasizes code readability with its notable use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
'''
