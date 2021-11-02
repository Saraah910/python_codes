'''Que: Write a Python program to check whether a character is uppercase or lowercase alphabet.
Name: Sakshi Aherkar
Roll no: 1047
Batch:A2
**************************************************'''

a=input("Entre any character: ")
# b=a.upper()
# c=a.lower()
if a.isupper():
    print("The entered character is in uppercase")
elif a.islower():
    print("The entered character is in lowercase")
else:
    print("The character is not an alphabet")
d=ord(a)   
print("The ascii value of the entered alphabet is: ",d)
    