# Create a class programmer for storing information of few programmers working at microsoft
class Programmers:
    CompanyName ="Microsoft"
    
    def __init__(self,Name,Language,Salary) -> None:
        self.Name=Name
        self.Language=Language
        self.Salary=Salary

        
    def printdetails(self):
        print(f"Name of the Employee:{self.Name}")
        print(f"Programming Language of the Employee:{self.Language}")
        print(f"Salary of the Employee:{self.Salary}")
        print(f"CompanyName of the Employee:{self.CompanyName} \n")

print("1st Employee Details")
Emp1=Programmers("Andrew","Python",190000)
Emp1.printdetails()

print("2nd Employee Details")
Emp2=Programmers("Sam","C#",230000)
Emp2.printdetails()

print("3rd Employee Details")
Emp3=Programmers("Nick Jones","Java",190000)
Emp3.printdetails()


#Write a class calculator capable of finding square , cube and squareroot of a number
