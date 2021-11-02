class Employee:
    company="Google"
    def showDetails(self):
        print("This is an Employee")
class programmer(Employee):
    post= "web developer"
    def getPost(self):
        print(f"The post of the programmer is {self.post}")
    def showDetails(self):
        print("This is an Programmer")
E= Employee()
p= programmer()
E.showDetails()
p.getPost()
print(p.company)
p.showDetails()
