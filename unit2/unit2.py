# Object Oriented Programming

class BankAccount:
    bank_name = "PayPy"

    def __init__(self, balance=0):
        self.balance = balance

    def deposite(self, amount):
        """The method will get amount of money and add it to the bank account."""
        self.balance += amount

    def withdraw(self, amount):
        """The method will get amount of money and subtract it from the bank account."""
        self.balance -= amount

    def print_balance(self):
        print("Current balance is: ", self.balance, '\n')

    def greet(self, name):
        print("Welcome", name, '\n')


def main():
    michals_account = BankAccount()
    print(michals_account)
    michals_account.greet("Michal")

    amirs_account = BankAccount()
    print(amirs_account)
    amirs_account.greet("Amir")

    eden = BankAccount()
    eden.greet("Eden")
    eden.deposite(1200)
    eden.withdraw(300)
    eden.print_balance()

    # Account with no previous amount of money.
    no_prev_money_acc = BankAccount()

    # Account with previous amount of money.
    with_prev_money_acc = BankAccount(2000)

    no_prev_money_acc.deposite(1)
    with_prev_money_acc.deposite(1)
    no_prev_money_acc.print_balance()
    with_prev_money_acc.print_balance()

    print(eden.balance)
    eden.balance = 0
    print(eden.balance)

    print(BankAccount.bank_name)   # By Class Name
    print(eden.bank_name)  # By object


if __name__ == "__main__":
    main()
