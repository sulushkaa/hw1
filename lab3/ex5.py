class Owner:
    def __init__ (self, first, last):
        self.first = first
        self.last = last
        print("Account owner:", self.first,  self.last)

class Balance(Owner):
    def __init__(self, first, last, initial_balance=0):
        super().__init__(first, last)
        self.balance = initial_balance

    def deposit (self, amount):
        if amount > 0 :
           self.balance += amount
           print("Your current balance is:", self.balance)
        else :
           print("Please, enter a valid deposit amount")
    def withdraw (self, amount):
         if amount > 0 and amount <= self.balance :
            self.balance -= amount
            print("Your current balance is:", self.balance)
         else :
             print("The withdraw amount exceeds current balance. Please, enter a valid amount:")


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
initial_balance = float(input("Enter your in7itial balance: "))

account = Balance(first_name, last_name, initial_balance)

    
deposit_amount = float(input("Enter your deposit amount: "))
account.deposit(deposit_amount)


withdraw_amount = float(input("Enter your withdrawal amount: "))
account.withdraw(withdraw_amount)


    