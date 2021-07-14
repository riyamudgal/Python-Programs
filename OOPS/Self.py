
class Employee:
    Company="apple"
    def getsalary(self):
        print("Salary is 190K")

Emp1=Employee()
Emp1.getsalary()
#Employee.getsalary(Emp1)                 #because of self
Emp2=Employee()
#Emp2.getsalary()                         #normal instance attribute
Employee.getsalary(Emp2)                  #because of self


class Employe:
    Company="Apple"
    def getSalary(self):
        print(f"Salary of employee working in {self.Company} is {self.Salary}")

Em1=Employe()

Em1.Company="Cisco"
Em1.Salary=4500000
Em1.getSalary()
#Employe.getSalary(Emp1)                 #because of self

Em2=Employe()

Em2.Company="Microsoft"
Em2.Salary=4520000
#Emp2.getSalary()                         #normal instance attribute
Employe.getSalary(Em2)                  #because of self
    
