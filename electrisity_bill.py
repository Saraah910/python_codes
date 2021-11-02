Total_units = int(input("Entre the total units:"))
amount1 = 0.5*50
a = (Total_units-50)*0.75
y = (Total_units-150)*1.25
amount2 = 0.75*100
def Bill():
    if Total_units<50:
        x = 0.5*Total_units
        print("Electrisity bill occured is:",x)
    elif Total_units>=50 and Total_units<=100: 
        print("Electrisity bill occured is:",(amount1+a))
    elif Total_units>=100 and Total_units<=200:
            if (Total_units-50)<=100:
                print("Electrisity bill occured is:",(amount1+a))
            elif(Total_units-50)>100:
                print("Electrisity bill occured is:",amount1+amount2+y)
    elif Total_units>=200 and Total_units<=250:
            #if (Total_units-150)<=100:
        print("Electrisity bill occured is:",amount1+amount2+y)
    else:
        print("Electrisity bill occured is:",Total_units*1.5)

obj = Bill()
print(obj)
  
    



  

