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
        
