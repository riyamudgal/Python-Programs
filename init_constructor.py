'''
class Customer:
    ID= "C01"
    Department="HR"
    def salary(self):
        print(f"Salary of Employee handling that Customer is {self.Salary}")


    def __init__(self):
        print("I'm like a constructor, I'm called implicitly")

    @staticmethod                     #static method decorator
    def staticFunction():              #there is no need to mention self in static method
        print("He is a good Customer")

cust=Customer()
cust.Salary="1000k"
Customer.salary(cust)               #calling of salary

Customer.staticFunction()            #calling of static method
'''


#initialising the parameters in init constructor
class Student:
     def __init__ (self,Name,Age,DOB):
         self.Name=Name
         self.Age=Age
         self.DOB=DOB

     def getDetails(self):
         print(f"Name of the Student is:{self.Name}")
         print(f"Age of the Student is:{self.Age}")
         print(f"DOB of the Student is:{self.DOB}")

St1=Student("Chia",17,"11-09-2004")
St1.getDetails()
