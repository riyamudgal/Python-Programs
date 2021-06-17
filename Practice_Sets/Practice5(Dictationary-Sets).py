#hindi to english translation
Translation={"pagal":"idiot",   
            "sundar":"beautiful",
            "phela":"first",
            "koshish":"try",
            "akl":"intelligent"}
print("Choose among the following options: \n ",Translation.keys())
a=input("Enter your Hindi Word\n")
print("The meaning pf entered word is :",Translation[a])     


#input 8 numbers and display unique ones
a1=input("Enter first number")
a2=input("Enter second number")
a3=input("Enter third number")
a4=input("Enter fourth number")
a5=input("Enter fifth number")
a6=input("Enter six number")
a7=input("Enter seven number")
a8=input("Enter eigth number")

set={a1,a2,a3,a4,a5,a6,a7,a8}
print(set)

#input two data-types in set
integer=input("Enter integer value")
string=input("Enter the string value")
float=input("Enter any float value")

set={integer,string,float}
print(set)                                     #set is heterogenous data-type

#calculating length of set after performing some calculations
from set_methods import A


emptyset=set()
emptyset.add(23)
emptyset.add("Adding")
print(len(emptyset))

#fav language entered by user in dictionary
favlang={}
a=input("Enter your fav. language Ram \n")
b=input("Enter your fav. language Ravan \n")
c=input("Enter your fav. language Sita  \n")
d=input("Enter your fav. language Laxman \n")
e=input("Enter your fav. language Hanuman \n")
favlang["Ram"]=a
favlang["Ravan"]=b
favlang["Sita"]=c
favlang["Laxman"]=d
favlang["Hanuman"]=e
print(favlang)

#can u change the v alue of inside a list which is contained in a set
set={34,56,99,"tom",[1999]}
print(set)
