#problem 1
var=input()
print("Good AfterNoon ", var)


#Alternative method
letter='''Dear <|Name|>,
You are selected!
Date: <|Date|>'''
name=input("Enter name")
date=input("Enter date")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)

#problem 3 replcae double spaces with single
story="once upon atime there is riya  named animal who is very  cruel and she beat everyone"
print(story.replace("  "," "))

#problem 4 detect double spaces
story="once upon atime there is riya  named animal who is very  cruel and she beat everyone"
print(story.find("  "))

#format a letter using escape sequence
letter='''Dear <|Name|>,\n \t You are selected!\n Date: <|Date|>'''
print(letter)
