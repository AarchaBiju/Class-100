class atm():
    def __init__(self,CardNumber,Pin):
       self.CardNumber = CardNumber
       self.Pin = Pin

    def CashWithDrawal(self):
        print("CashWithDrawal")   

    def BalanceEnquiry(self):
        print("BalanceEnquiry")    
        
Aarcha = atm(1234, 2707)
Aarcha.CashWithDrawal()
Aarcha.BalanceEnquiry()
