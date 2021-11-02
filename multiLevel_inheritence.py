class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing")

    def __init__(self):
        print("Initializing person:")

class Employee(Person):
    company = "Google"
    def getSalary(self):
        print(f"The salary is {self.sakalry}")

    def takeBreath(self):
        print("I am breathing luckily")

    def __init__(self):
        super().__init__()
        print("Initializing Empolyee:")

class Programmer(Employee):
    company = 'Fiverr'
    def getSalary(self):
        print("There is no salary to programmers")
    def takeBreath(self):
        super().takeBreath()
        print("I am breathing luckily the fresh air")


p = Person()
p.takeBreath()

e = Employee()
e.takeBreath()

pr = Programmer()
print(p.country)
pr.takeBreath()
