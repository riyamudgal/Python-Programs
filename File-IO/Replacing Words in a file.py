#a file contains word "Donkey" multiple times. you need to write a program which replaces this word with ##### by updating the same file
with open("poem.txt") as f:                   #reading poem.text
    language=f.read()                         #storing contents in a variable
language=language.replace("hell","#$#$")
with open("poem.txt",'w') as f:
    f.write(language)


#repeat above program for a list of such words to be censored
words=["poor","bad","hell"]
with open("poem.txt") as f:
    variable=f.read()
for word in words:
    variable=variable.replace(word,"#$#$#")
with open("poem.txt", 'w') as f:
    f.write(variable)
