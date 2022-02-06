class StudentDetails:
    detailstype="StudentDetails"
    def printData(self):
        print(f"Name is {self.Name}")
        print(f"Course is {self.course}")
        print(f"Year is {self.year}")

print("Details of Student 1:  ")
student1=StudentDetails()
student1.Name="Sanjay"
student1.course="B.Tech"
student1.year="3rd"
student1.printData()        
print("Details of Student 2:  ")
student1=StudentDetails()
student1.Name="Rajeev"
student1.course="MCA"
student1.year="2nd"
student1.printData()        
print("Details of Student 3  ")
student1=StudentDetails()
student1.Name="Deepak"
student1.course="MBA"
student1.year="1st"
student1.printData()        