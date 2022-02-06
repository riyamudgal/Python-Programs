'''#reading text from a given file and finding a particular word
f=open("poem.txt","r")
t=f.read()
f.close()
a=t.find("twinkle")
print(a)

#the game() function in a program lets a user play a game and returns the score as an integer. you need to read a file 'hiscore.txt'
#which is contains the previous hi-score you need to write a program to update the hi-score whenever game() breaks the Hi-score
def game():
    return 100

score=game()                                          #storing the returned value by the function in a variable

with open("highscore.txt") as file:                   #opening a file, storing the value of newscore
    newscore=int(file.read())                         #reading content and then storing it in variable, typecasting it into int

if(newscore<score):                                   #comparing the values, if newscore is smaller
    with open("highscore.txt", "w") as file:          #opening the text file in writing mood
        file.write(str(score))                        #then the value stored is over-ridden, by typecasting it into str, because file takes string type data


#the game() function in a program lets a user play a game and returns the score as an integer. you need to read a file 'hiscore.txt'
#which is either blank or contains the previous hi-score you need to write a program to update the hi-score whenever game() breaks the Hi-score
def game():
    return 100

score=game()                                     #storing the returned value by the function in a variable

with open("highscore.txt") as file:              #opening a file, storing value of newscore
    newscore=file.read()                         #reading content and then storing it in variable, typecasting is not done here, we will do it at the time of comparison


if newscore=='':                                 #checking if file is blank
    with open("highscore.txt", "w") as file:     #opening the text file in writing mood
        file.write(str(score))                   #then the score value is stored in the file, by typecasting it into str, because file takes string type data

elif int(newscore)<score:                        #if file is not blank then comparing the values, typecasting is done for integer only, not for blank space
    with open("highscore.txt", "w") as file:     #opening the text file in writing mood
        file.write(str(score))                   #then the value stored is over-ridden, by typecasting it into str, because file takes string type data
        

# write a program to generate multiplication tables from 2 to 20 and write it to the different files . place these files in a folder for a 13- year old student
for i in range(2,21):                                      #loop for number 
    with open(f"Tables/Table-of-{i}.txt","w") as a:        # opening a folder(files),Folder name-Tables, for each number different file will be created naming "Table-of-i.txt" in the folder
        for j in range(1,11):                              
            a.write(f"{i}*{j}={i*j}")                      #for printing table
            if(j!=10):                                     #for cursor to stop at 10
             a.write('\n')


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
    

#log file
with open("log.txt") as f:
    content=f.read()
if "Company" in content.lower():
    print("yes company is present")
else:
    print("company is not present")


# write a program to make a copy of a text file "this.txt"
with open("TextFile.txt") as file:                     #open a file whose content will be copied to a new file
    content=file.read()                                 #copying content

with open("Copy.txt",'w') as file:                     #open another file in writing mode in which we are going to copy contents of above file
    file.write(content)

# write a program to find out whether a file is identical & matches the content of another file
file1="TextFile.txt"                           #storing first file name in file1 variable
file2="Copy.txt"                               #storing second file name in file2 variable

with open (file1) as f:                        #open file using file variable
    content1=f.read()                          #storing contents of file1 in content1

with open (file2) as f2:
    content2=f2.read()                         #storing contents of file2 in content2

if content1==content2:                         #comapring contents of two files
    print("Files are identical")
else:
    print("Files are not identical")
'''

# write a program to wipe out the contents of a file using python
filename="TextFile.txt"

with open (filename, 'w') as f:
    f.write(" ")
    
'''
#write a program to rename a file
#first we are copying the contents of the file into another file, then we will delete the old file.Hence this is a way of renaming a file
#importing the os moduleand using os.remove("filename.tex") will remove/delete the file which name has been specified in the ()
import os
oldname="Samplefile.txt"
newname="Renamed-file.txt"

with open (oldname) as f:
    contents=f.read()

with open (newname,'w') as f:
    f.write(contents)

os.remove(oldname)
'''
