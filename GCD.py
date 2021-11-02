num1 = int(input("Entre the number:"))
num2 = int(input("Entre the number:"))
l1, l2,l3 = [], [], []
for i in range(1,num1+1):
    a = num1 % i
    if a==0:
        l1.append(i)
print(l1)
for j in range(1,num2+1):
    b = num2 % j 
    if b==0:
        l2.append(j)
print(l2)
for k in l1:
    for m in l2:
        if k == m:
            if len(l1) > len(l2):
                z = k
            else:
                z = m
print(z)
    
            
            

