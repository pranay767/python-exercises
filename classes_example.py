class BankAccount:
    def __init__(self, balance, acc_no):
        self.acc_no = acc_no
        self.__balance = balance
    def __repr__(self):
        return f"acc no: {self.acc_no}\nbalance: {self.__balance}"


account102 = BankAccount(2000, 233)

account102.acc_no = 900
account102.__balance = 800
print(account102)