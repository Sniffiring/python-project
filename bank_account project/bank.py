class bank:
    def __init__(self,bal,acc):
        self.balance = bal
        self.accountNo = acc

    def debit(self,amount):
        self.balance += amount
        print(f"Rs",amount,"amount is debited",)
        print(self.totl_amt())

    def totl_amt(self):
        return self.balance
    
           


acc1=bank(10000,5432)
acc1.debit(500)


