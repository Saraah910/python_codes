class Employee:
    company= "Google"
    def getSalary(self,signature):
        print(f"The salary is {self.salary} and the company is {self.company}" )
    def greet(self):
        print("Good morning sir!!")
    def time(self):
        print("9 AM in morning")
Sakshi = Employee()
Sakshi.salary=500000
Sakshi.getSalary('Thanks!!')
Sakshi.greet()
Sakshi.time()
