'''#Create a class programmer for sorting information of few programmers working at microsoft
class Programmer:
    Company= "Microsoft"
    def __init__(self, Id, Name, Language, DOJ):
        self.Id=Id
        self.Name=Name
        self.Language=Language
        self.DOJ=DOJ

    def printInfo(self):
        print(f" Id of employee is ->{self.Id} \n Name of Employee is ->{self.Name} \n Langauge -> {self.Language} \n DOJ is -> {self.DOJ} \n")

P1=Programmer("MS987", "Harry", "Java", "19/07/2014")
P2=Programmer("MS547", "William", "C#", "24/11/2017")
P3=Programmer("MS675", "Sam", "C++", "11/02/2019")
P4=Programmer("MS091", "Michael", "SQL", "02/09/2007")
P5=Programmer("MS021", "Christanio", "python", "29/05/2016")

print("\n Information of first programmer ")
P1.printInfo()
print("\n Information of second programmer ")
P2.printInfo()
print("\n Information of third programmer")
P3.printInfo()
print("\n Information of fourth programmer")
P4.printInfo()
print("\n Information of fifth programmer ")
P5.printInfo()

'''
#Write a class calculator capable of finding square , cube and squareroot of a number
class Calculator:
    def __init__(self, num1):
        self.num1=num1

    def Square(self):
        print(f" Square of {self.num1} is {self.num1**2}")

    def Cube(self):
        print(f" Cube of {self.num1} is {self.num1**3}")

    def SquareRoot(self):
        print(f" SquareRoot of {self.num1} is {self.num1**0.5}")

Num=Calculator(9)
Num.Square()
Num.Cube()
Num.SquareRoot()





