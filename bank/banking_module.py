from customer_module import Customer

class Banking(Customer):
    """ Banking class with has base/super/parent class as a Customer """

    def __init__(self, accountNo):
        self.accountNo = accountNo

    def Balance(self):
        """ Balance method return a customer dict """
        customer = super().FetchCustomer(self.accountNo)
        if customer:
            return customer
        return False

    def Deposite(self, amount):
        customerBalance = self.Balance()
        if customerBalance:
            amount = int(customerBalance["balance"]) + int(amount)
            return super().UpdateBalance(self.accountNo, amount)
        return False

    def withDraw(self, amount):
        customerBalance = self.Balance()
        if customerBalance:
            amount = int(customerBalance["balance"]) - int(amount)
            return super().UpdateBalance(self.accountNo, amount)
        return False
