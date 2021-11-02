class Employee:
    company="Google"
    ecode=120
    def upgradeEcode(self):
        self.ecode=self.ecode*100

class Freelancer:
    company="Fiver"
    level=10
    def upgradeLevel(self):
        self.level=self.level+1

class programmer(Freelancer,Employee):
    name="Sakshi"

p=programmer()
p.upgradeLevel()
print(p.company)