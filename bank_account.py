class BankAccount:
    def __init__(self, kind, pin):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees = 0
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount, pin_from_user):

        if(self.pin == pin_from_user):
            if(self.balance < amount):
                print("Sorry you don't have that amount in your account")
                return 
            elif (self.balance == amount):
                self.balance -= amount
                print("You are now BROKE!!")
            else:
                self.balance -= amount
                print("Current Balance is now {}".format(self.balance))
                return

        else: 
            print("The pin number is incorrect. Please try again.")
        # if (self.balance < 0):
        #     self.overdraft_fees += 36
        # return amount

    def change_pin(self, pin):
        self.pin = pin
        print(f"The new pin number is {self.pin}")



vin_checking = BankAccount("checking", 1234)
print("My new account is a {} account".format(vin_checking.kind))

vin_checking.deposit(5000)
# print("My current balance is ${}.".format(vin_checking.balance))

vin_checking.withdraw(2500, 1235)
# print("My current balance is ${}.".format(vin_checking.balance))

vin_checking.withdraw(2600, 1234)
# print("My overdraft fee is currently {}".format(vin_checking.overdraft_fees))
# print("My current balance is ${}.".format(vin_checking.balance))

vin_checking.change_pin(2221)