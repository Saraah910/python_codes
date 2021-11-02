UserName=str(input("Entre the username: "))
#print("The Username has ", len(UserName)," charecters")
a=len(UserName)
if(a<=10):
    print("You need a strong username.")
else:
    print("Username is saved.")
