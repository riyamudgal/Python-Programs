word = input("Input a word to reverse: ")
print("Reversed String is -> ")
for ch in range(len(word)-1, -1, -1):
  print(word[ch], end=" ")

  
'''
Output
Input a word to reverse: happyworld 
Reversed String is ->
d l r o w y p p a h
'''

#no blank spaces in output
word = input("Input a word to reverse: ")
print("Reversed String is -> ")
for ch in range(len(word)-1, -1, -1):
  print(word[ch], end=" ")
print("\n")

'''
Output
Input a word to reverse: happyworld 
Reversed String is ->
dlrowyppah
'''


#range function starts from from len-1, should stop at 0 index but second parameter integer number specifying at 
#which position to stop is not included(so that's why we have taken -1), third -1 is for reversing
