class number:
    def __init__(self,num):
        self.num = num 
    def __add__(self,num2):
        print(f"Lets add")
        return self.num + num2.num
    def __mul__(self,num2):
        print(f"Let's multiply")
        return self.num * num2.num

x = number(45)
y = number(200)
sum = x + y
print(sum)
mul = x * y
print(mul)


