def Bill():
    if Total_units<50:
        x = 0.5*Total_units
        print("Electrisity bill occured is:",x)
    elif Total_units>=50 and Total_units<=100: 
        per = (amount1+a)*0.17+(amount1+a)
        print("Electrisity bill occured is:",per)
    elif Total_units>=100 and Total_units<=200:
        if (Total_units-50)<=100:
            per = (amount1+a)*0.17+(amount1+a)
            print("Electrisity bill occured is:",per)
        elif(Total_units-50)>100:
            per = (amount1+amount2+y)*0.17+(amount1+amount2+y)
            print("Electrisity bill occured is:",per)
    elif Total_units>=200 and Total_units<=250:
        per = (amount1+amount2+y)*0.17+(amount1+amount2+y)
        print("Electrisity bill occured is:",per)
    else:
        print("Electrisity bill occured is:",Total_units*1.5)
    


Total_units = int(input("Entre the total units:"))
amount1 = 0.5*50
a = (Total_units-50)*0.75
y = (Total_units-150)*1.25
amount2 = 0.75*100
Bill()
  
    



  

