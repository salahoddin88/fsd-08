class Customer:
    """ Customer class with customers attribute """

    customers = []

    def FetchAllCustomer(self):
        """ Fetch All customers """
        return self.customers

    def FetchCustomer(self, accountNo):
        """  Fetch Single customer based on account no """
        for customer in self.customers:
            if customer['accountNo'] == accountNo:
                return customer

        return False

    def Register(self, name, accountNo):
        """ Register customer with name and account No. and make initial balance 0 """
        checkExistingCustomer = self.FetchCustomer(accountNo)
        if checkExistingCustomer == False:
            customerDict = {
                'name': name,
                'accountNo': accountNo,
                'balance': 0
            }

            self.customers.append(customerDict)
            return customerDict
        else:
            print('Customer already exist with same account no')

    def UpdateBalance(self, accountNo, amount):
        """  Update Customer's balance based on Amount """
        for key, customer in enumerate(self.customers):
            if customer['accountNo'] == accountNo:
                self.customers[key]['balance'] = amount
                return customer
        return False
