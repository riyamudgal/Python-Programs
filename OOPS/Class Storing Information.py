#Create a class programmer for sorting information of few programmers working at microsoft
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



'''Output
Information of first programmer
 Id of employee is ->MS987
 Name of Employee is ->Harry
 Langauge -> Java
 DOJ is -> 19/07/2014


 Information of second programmer
 Id of employee is ->MS547
 Name of Employee is ->William
 Langauge -> C#
 DOJ is -> 24/11/2017


 Information of third programmer
 Id of employee is ->MS675
 Name of Employee is ->Sam
 Langauge -> C++
 DOJ is -> 11/02/2019


 Information of fourth programmer
 Id of employee is ->MS091
 Name of Employee is ->Michael
 Langauge -> SQL
 DOJ is -> 02/09/2007


 Information of fifth programmer
 Id of employee is ->MS021
 Name of Employee is ->Christanio
 Langauge -> python
 DOJ is -> 29/05/2016
 '''
