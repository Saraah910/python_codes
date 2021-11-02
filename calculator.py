class calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"The square of the {self.num} is {self.num**2}")
    def cube(self):
        print(f"The cube of the {self.num} is {self.num**3}")
    def squareroot(self):
        print(f"The squareroot of the {self.num} is {self.num**0.5}")
    @staticmethod
    def greet():
        print("Hello and welcome to the best calculator of all time")
a=calculator(9)
a.square()
a.cube()
a.squareroot()
a.greet()
