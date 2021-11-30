
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
                'accountNo' : accountNo,
                'balance' : 0
            }

            self.customers.append(customerDict)
            return customerDict
        else:
            return 'Customer already exist with same account no'


    def UpdateBalance(self, accountNo, amount):
        """  Update Customer's balance based on Amount """
        for key, customer in enumerate(self.customers):
            if customer['accountNo'] == accountNo:
                self.customers[key]['balance'] = amount
                return customer
        return False


class Banking(Customer):
    """ Banking class with has base/super/parent class as a Customer """

    def __init__(self, accountNo):
        self.accountNo = accountNo


    def Balance(self):
        customer = super().FetchCustomer(self.accountNo)
        if customer:
            return customer["balance"]
        return False


    def Deposite(self, amount):
        customerBalance = self.Balance()
        if customerBalance:
            amount = int(customerBalance) + int(amount)
            x = super().UpdateBalance(self.accountNo, amount)
            return x
        return False


    def withDraw(self, amount):
        customerBalance = self.Balance()
        if customerBalance:
            amount = int(customerBalance) - int(amount)
            x =  super().UpdateBalance(self.accountNo, amount)
            return False



operation = 0
while operation != 9:

    bankOperation = 0

    print(''' 
        1. Register Customer
        2. Print All Customer
        3. Banking Operation
        9. Exit
    ''')

    operation = int(input(" Select Operation "))

    if operation == 1:
        """ Registration """
        name = input(" Enter Customer's Name: ")
        accountNo = input(" Enter Account No: ")

        customer = Customer()
        customer.Register(name, accountNo)

    elif operation == 2:
        customer = Customer()
        customerData = customer.FetchAllCustomer()

        for singleCustomer in customerData:
            print("{} - {} - {}".format(singleCustomer['name'], singleCustomer['accountNo'], singleCustomer['balance']))

    elif operation == 3:
        accountNo = input("Please Enter Customer's Account No. : ")
        banking = Banking(accountNo)
        customerData = banking.FetchCustomer(accountNo)
        if customerData:
            
            while bankOperation != 9:
                print(f'Welcom {customerData["name"]}')
                print('''
                    1. Balance
                    2. Deposite
                    3. WithDraw
                    9. Back
                ''')
                bankOperation = int(input('Select Banking Operation: '))
                
                if bankOperation == 1:
                    customerBalance = banking.Balance()
                    print(customerBalance)
                    print(f"Customer's balance is: {customerBalance}")
                elif bankOperation == 2:
                    amount = int(input('Please Enter Amount to be deposite: '))
                    x = banking.Deposite(amount)

                    print(f'success {x}')
                elif bankOperation == 3:
                    amount = int(input('Please Enter Amount to be withdraw: '))
                    banking.withDraw(amount)
                    print(f'success {x}')
                elif bankOperation == 4: 
                    print('bye')
                else:
                    print('Invalid Option')
        else:
            print("No data Found")



