class LunchCard:

    def __init__(self, init_balance, id, name):
        self.balance = init_balance
        self.id = id
        self.name = name
    
    def payLunch(self, bill_amount): # setter
        if isinstance(bill_amount, int) or isinstance(bill_amount, float):
            if bill_amount <= self.balance:
                self.balance -= bill_amount
                print("Payment is successful for", self.name)
            else:
                print("You don't have enough credit to pay for this lunch!")
        else:
            print("bill_amount should be numerical value!")
    
    def depositMoney(self, deposit): # setter
        if isinstance(deposit, int) or isinstance(deposit, float):
            if deposit > 0:
                self.balance += deposit
            else:
                print("deposit should be a positive value")
        else:
            print("deposit should be numerical value!")
    
    def displayCurrentBalance(self): # getter
        print("Current balance for", self.name, "is", self.balance)
        
