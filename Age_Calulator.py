from datetime import date
from tkinter import * 
from tkinter import ttk

def calculateAge():
    today = date.today()
    print(today)
    birthDate = date(int(ety_year.get()), int(ety_month.get()), int(ety_day.get()))
    print(birthDate)
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    print(age)
    Label(text=f'{ety_name.get()}, your age is {age}', font=('times new roman', 15, 'bold')).place(x=160, y=250)


root = Tk()
root.geometry('500x300+0+0')
root.title('Age Calculator')

dateName = StringVar()
dateYear = StringVar()
dateMonth =StringVar()
dateDay = StringVar()

lbl_name = Label(root, text='Name', font=('times new roman', 15, 'bold'))
lbl_name.place(x=130, y=45)
ety_name = ttk.Entry(root, width=20, textvariable=dateName)
ety_name.place(x=200, y=50)

lbl_year = Label(root, text='Year', font=('times new roman', 15, 'bold'))
lbl_year.place(x=130, y=80)
ety_year = ttk.Entry(root, width=20, textvariable=dateYear)
ety_year.place(x=200, y=85)

lbl_month = Label(root, text='Month', font=('times new roman', 15, 'bold'))
lbl_month.place(x=130, y=115)
ety_month = ttk.Entry(root, width=20, textvariable=dateMonth)
ety_month.place(x=200, y=120)

lbl_day = Label(root, text='Day', font=('times new roman', 15, 'bold'))
lbl_day.place(x=130, y=150)
ety_day = ttk.Entry(root, width=20, textvariable=dateDay)
ety_day.place(x=200, y=155)

btn_calculate = ttk.Button(root, text='Calculate Age', width=20, command=calculateAge)
btn_calculate.place(x=190, y=200)

root.mainloop()