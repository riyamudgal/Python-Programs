'''Bob has just turned 18 years old and has opened a Bank account. However, since he has just opened his bank account he is not very experienced about 
the working of banks, therefore he asks for your help. Bob wants to know whether the IFSC Code given by the bank is valid or not, can you help him? 
A valid IFSC (Indian Financial System) Code must be of the following format:- 
  1) The string should be 11 characters long. 
  2) The first four characters of the IFSC Code should be upper case alphabets. 
  3) The fifth character should be 0. 
  4) The last six characters should be alphanumeric.

SAMPLE INPUT 
59587947263620425540520450385RFJHQ

SAMPLE OUTPUT 
False'''

import re
account=input()
flag=0
while True:
    if len(account)!=11:
        flag=-1
        break
    elif not re.search("^[A-Z]{4}0[A-Z0-9]{6}$", account):
        flag=-1
        break
    else:
        flag=0
        print("True")
        break

if flag==-1:
    print("False")
