from atm_card import ATMCard

class Customer:
    def __init__(self, id, custPin=1234, custBalance=10000):
        self.id = id
        self.pin = custPin
        self.balance = custBalance
    def cek_id(self):
        return self.id
    def cek_custPin(self):
        return self.pin
    def cek_custBalance(self):
        return self.balance
    def withdrawBalance(self, nominal):
        self.balance -= nominal
    def depositBalance(self, nominal):
        self.balance += nominal
    