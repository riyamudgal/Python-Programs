'''
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [!@#$&*].
Minimum length 6 characters.
Maximum length 16 characters.


Python has a built-in package called re, which can be used to work with Regular Expressions.
After importing the re module, we can start using regular expressions
search	Returns a Match object if there is a match anywhere in the string(re.search())

\s -->	Returns a match where the string contains a white space character	--> "\s"
[]	--> A set of characters	--> "[a-m]"

'''

import re
while True:
    password=input("Enter your password")
    flag=False
    if len(password)<6 or len(password)>16:
        print("Not valid!, Total characters should be between 6 and 16")
        continue
    elif not re.search("[A-Z]", password):
        print("Not valid!, It should contains atleast one letter in upper case [A-Z]")
        continue
    elif not re.search("[a-z]", password):
        print("Not valid!, It should contains atleast on letter in lower case [a-z")
        continue
    elif not re.search("[0-9]", password):
        print("Not valid!, It should contains atleast a number between 0 and 9")
        continue
    elif not re.search("[!@#$&*]", password):
        print("Not valid!, It should contains atleast one special character")
        continue
    
    else:
        flag=True
        break
        
if flag==True:
    print("Valid Password")
    
    
#blank space condition has been taken into consideration
