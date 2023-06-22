class Wallet:

    # first thing to run when we make a new class
    # outline required user-provided input values here
    def __init__(self, initial_amount=0):
        # save the user-provided initial amount as an attribute
        # self refers to whatever object I'm working with
        self.balance = initial_amount

    def spend(self, amount):
        if self.balance < amount:
            return "not enough money!"
        else:
            self.balance = self.balance - amount
            return f"${amount} spent. Remaining balance: ${self.balance}"
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        return f"${amount} added. New balance: ${self.balance}"

    # __repr__ method
    # changes how the "object" looks when it is printed out
    def __repr__(self):
        return f"Wallet with balance of: ${self.balance}"
    


if __name__ == '__main__':
    wallet1 = Wallet(150)
    wallet2 = Wallet(3000)
    wallet3 = 50

    print(wallet1.balance)
    print(wallet1.spend(120))
    print(wallet1.deposit(50))
    print(wallet1.spend(60))
    print(wallet1.balance)

    print(wallet1)
    print(wallet2)
    print(wallet3)