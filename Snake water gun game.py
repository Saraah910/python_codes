import random
import tkinter

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
    elif comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True
print("Comp turn: 'Rock(r), Paper(p) or Siccors(s):")
randNo=random.randint(1,3)
#print(randNo)
if randNo==1:
    comp = 'r'
elif randNo==2:
    comp = 'p'
else:
    comp = 's'

you=input("Player 2 turn: Rock(r), Paper(p) or Siccors(s): ?")
a=gameWin(comp,you)
print("Computer choose ",comp)
print("you choose ",you)
if a ==None:
    print("The game is tie")
elif a:
    print("You win !!")
else:
    print("You lose!!")
