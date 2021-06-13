#find greatest among 4 numbers 
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
d=int(input("enter fourth number"))
if(a>b and a>c and a>d):
    print(a," is greatest")
elif(b>c and b>d):
    print(b," is greatest") 
elif(c>d):
    print(c," is greatest")
else:
    print(d," is greatest")


# report card
sub1=int(input("enter the marks of first subject"))
sub2=int(input("enter the marks of second subject"))
sub3=int(input("enter the marks of third subject"))
average=((sub1+sub2+sub3)/300)*100
print("average marks obtained by a student is :", average)
if(sub1>=33 and sub2>=33 and sub3>=33 and average>=40):
    print("student is pass")
else:
    print("student is fail")

 #checking spam
text=input("enter the text")
if("make lot of money" in text):
    spam= True
elif("subscribe now" in text):
    spam= True
elif("click this" in text):
    spam= True
elif("buy now" in text):
    spam= True
else:
    spam= False
if(spam):
    print("this statement is a spam")
else:
    print("this statement is not a spam")

#length of the character
name="communication" 
a=len(name)
if(a<=10):
    print("true")
else:
    print("false")


#list
names=["virat","rohit","dhoni","boult","pollard"]
if("hardik" in names):
    print("valid")
else:
    print("invalid")


#student grading
m1=int(input("enter marks"))
if m1>=90:
    print("Ex")
elif m1>=80:
    print("A")
elif m1>=70:
    print("B")
elif m1>=60:
    print("C")
elif m1>=50:
    print("D")
else:
    print("Fail")


#searching string in a paragraph using in 
question="William Henry Gates III (born October 28, 1955) is an American business magnate, software developer, investor, author, and philanthropist. He is the co-founder of Microsoft Corporation."
if "harry" in question:
    print("Found")
else:
    print("not found")
