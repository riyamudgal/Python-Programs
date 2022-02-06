class Employee:
   company="Google"

Emp1=Employee()                         #object creation
Emp1.salary="30k"                       #assigning value to salary
Emp1.age=34                             #assigning value to age

print(Emp1.company)                     #printing companies name
print(Emp1.salary)                      #printing salary
print(Emp1.age)                         #printing age

Employee.company="Youtube"
print(Emp1.company)

