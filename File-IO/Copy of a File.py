# write a program to make a copy of a text file "this.txt"
with open("TextFile.txt") as file:                     #open a file whose content will be copied to a new file
    content=file.read()                                 #copying content

with open("Copy.txt",'w') as file:                     #open another file in writing mode in which we are going to copy contents of above file
    file.write(content)
