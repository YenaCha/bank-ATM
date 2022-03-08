class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin
    def displaybalance(self):
        print('your balance is '+str(self.balance))
    def cashwithdrawl(self):
        newpin = int(input('Enter your pin number'))
        if(newpin == self.pin):
            amt = int(input('How much do you want to withdrawl?'))
            if(amt <= self.balance):
                self.balance = self.balance-amt
                print('Withdrawl successful '+str(self.balance))
            else:
                print('Not enoughh money')
        else:
            print('pin incorrect')
    def cashdeposit(self):
        newpin = int(input('Enter your pin number'))
        if(newpin == self.pin):
            amt = int(input('How much do you want to deposit?'))
            self.balance = self.balance+amt
            print('Deposit successful '+str(self.balance))
            
            
        else:
            print('pin incorrect')

Yena = ATM(500, 1234)
# Yena.displaybalance()
# Yena.cashwithdrawl()
Yena.cashdeposit()