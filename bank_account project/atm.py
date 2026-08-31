class atm:
    def __init__(self,balance):
        self.balance = balance
    def menu(self):   
      while True:
       a = input("choose(withdrawal,Deposite,show_bal,exit)")
       if a == "withdrawal":
        amount = float(input("Enter withdrawal amount: "))
        self.withdrawal(amount)
       elif a == "Deposite":
        amount = float(input("Enter Deposite amount: "))
        self.Deposite(amount)
       elif a == "show_bal":
        self.show_bal()
       elif a == "exit":
        print("Exit")
        break 
    def Deposite(self,amount):
       self.balance += amount
       print(f"the amount is: ",self.show_bal())   

    def withdrawal(self,amount):
     if self.balance>= amount:
        self.balance-= amount
        print("totle balance is: ",self.show_bal())
     else:
        print("insufficient balance")
    def show_bal(self):
     print("totle balance is ", self.balance) 

option = input("Choose user (user1/user2) or type 'exit' to quit: ")    

if option == "user1":

    balance = float(input("Enter initial balance for User1: "))

    user1 = atm(balance)

    user1.menu()

elif option == "user2":

    balance = float(input("Enter initial balance for User2: "))

    user2 = atm(balance)

    user2.menu()

elif option == "exit":

    print("Goodbye!")
    

