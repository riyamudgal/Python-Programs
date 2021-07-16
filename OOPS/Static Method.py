class Customer:
    ID= "C01"
    Department="HR"
    def salary(self):
        print(f"Salary of Employee handling that Customer is {self.Salary}")

    @staticmethod                     #static method decorator
    def staticFunction():              #there is no need to mention self in static method
        print("He is a good Customer")

cust=Customer()
cust.Salary="1000k"
Customer.salary(cust)               #calling of salary

Customer.staticFunction()            #calling of static method
