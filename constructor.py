class Employee:
    company= "Google"
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("The employee is created")
    def getDetails(self):
        print(f"The name of the Employee is {self.name}")
        print(f"The salary of the Employee is {self.salary}")
        print(f"The subunit of the Employee is {self.subunit}")

Sakshi=Employee("sakshi",5000,"Youtube")
Sakshi.getDetails()
