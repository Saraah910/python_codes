class train:
    train="Rajdhani Express"
    def __init__(self,name,fares,seats) -> None:
        self.name=name
        self.fares=fares
        self.seats=seats
    def getStatus(self):
        print(f"The name of the train is: {self.name}")
        print(f"The fares of the train is: {self.fares}")
        print(f"The number of seats in the train are: {self.seats}")
    def bookTickets(self):
        if(self.seats>0):
            print(f"Your seat has been booked and your seat no is: {self.seats}")
            self.seats=self.seats-1
        else:
            print("Sorry the train is full.")
    def cancelTicket(self,seatNo):
        if(self.seats-1):
            print(f"The seat no {self.seat} has been cancelled")
        
Obj=train("Rajdhani Express:1024",50,5)
Obj.getStatus()
Obj.bookTickets()
Obj.bookTickets()
Obj.bookTickets()