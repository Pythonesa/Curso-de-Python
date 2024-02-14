from threading import Thread
from time import sleep

class BankAccount:
    def __init__(self):
        self.balance = 1000

    def withdraw(self, amount):
        current_balance = self.balance
        sleep(2)
        current_balance -= amount
        self.balance = current_balance
        print(f"Withdrew {amount} from account. Balance is now {self.balance}")


def withdraw_from_account(account, amount):
    for _ in range(5):
        account.withdraw(amount)

account = BankAccount()

t1 = Thread(target=withdraw_from_account, args=(account, 100))
t2 = Thread(target=withdraw_from_account, args=(account, 200))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Final balance: {account.balance}")