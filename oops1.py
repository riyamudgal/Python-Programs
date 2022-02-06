#class and instance attributes
class Employee:
    Name="Kook"
    Age=34
    Salary=120000
    Company="Microsoft" 

#Assigning values to E1 i.e., assigning values to instance attributes
E1=Employee()
E1.Name="Sam"
E1.Age=37
E1.Salary=2300000
E1.Company="Microsoft"

#printing the va;ues of E1
print(E1.Name)
print(E1.Age)
print(E1.Salary)
print(E1.Company)

E2=Employee()

#Since we have not assigned values to the instance attributes that's why the values from the class attributes are Stored in E2
print(E2.Name)
print(E2.Age)
print(E2.Salary)
print(E2.Company)



