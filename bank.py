""" banking system for one customer """

# name = "Mohit"
# balance = 500
# account_number = "123456"

# print('''1. Debit 
# 2. Credit''')
# operation = int(input("Select Your operation: "))
# amount = int(input("Enter Amount: "))

# if operation == 1:
#     if balance == 0:
#         print('Your account balance is 0')
#     elif balance >= amount:
#         balance = balance - amount
#         print(balance)
#     else:
#         print("Your balance is low")

# elif operation == 2:
#     balance = balance + amount
#     print(balance)

# else:
#     print("Invalid operation")



""" Banking system with dict """
customer = {'name' : "Vivek", 'account':'123456', 'balance': 1000}

accountNumber = input("Enter your account number: ")
operation = 0
if customer['account'] == accountNumber:
    while operation != 4:
        #banking code here
        print('''
        1. Debit
        2. Credit
        3. Balance
        4. Exit
        ''')
        operation = int(input("Enter operation: "))

        if operation == 1:
            amount = int(input("Enter amount for debit: "))
            # check if balance is zero or not
            if customer['balance'] == 0:
                print("Your balance is zero")
            
            #check if balance is greater than amount
            elif customer['balance'] >= amount:
                customer['balance'] = customer['balance'] - amount
                print(customer)
            else:
                print('Your balance is low')
        
        elif operation == 2:
            amount = int(input("Enter amount to credit: "))
            customer['balance'] = customer['balance'] + amount
            print(customer)

        elif operation == 3:
            print(customer['balance'])
        
        elif operation == 4:
            break

        else:
            print("Invalid Operation")
else:
    print('Invalid Account Number')
