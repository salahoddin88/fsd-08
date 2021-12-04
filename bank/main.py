from customer_module import Customer
from banking_module import Banking

def main():
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
                print("{} - {} - {}".format(singleCustomer['name'],
                    singleCustomer['accountNo'], singleCustomer['balance']))

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
                        print(
                            f"Customer's balance is: {customerBalance['balance']}")
                    elif bankOperation == 2:
                        depositeAmount = int(
                            input('Please Enter Amount to be deposite: '))
                        x = banking.Deposite(depositeAmount)

                        print(f'success')
                    elif bankOperation == 3:
                        withdrawAmount = int(
                            input('Please Enter Amount to be withdraw: '))
                        banking.withDraw(withdrawAmount)
                        print(f'success')
                    elif bankOperation == 4:
                        print('bye')
                    else:
                        print('Invalid Option')
            else:
                print("No data Found")


# Calling main function
main()