import random
database = {
    445694103: ['mercy', 'umoh', '0990', 'umi', 'iku', 800 ] 
}
balance = [700, 800, 600, 1000, 200000]
def init():
    isValidOptionSelected = False
    print('Welcome to Lemo Bank!!!')

    while isValidOptionSelected == False:

        haveacct = int(input('Do you have an account with us? \n 1 (yes) 2(no) \n '))
        if haveacct == 1:
            isValidOptionSelected = True
            login()
        elif haveacct == 2:
            isValidOptionSelected = True
            register()   
        else:
            isValidOptionSelected = False
            print('invalid option')


# register
def register():
    print('****Register here**** \n fill in your details')
    first_name = str(input('Fisrt Name: \n'))
    last_name = str(input('Last Name: \n'))
    phone_number = int(input('Phone Number: \n'))
    email = input('Email Address: \n')
    password = input('Password: \n')
    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, phone_number, email, password, 0]
    print('Your Account has been created')
    print('Your AccountId is', accountNumber)
    login()

 
#login
def login():
    print('*****Log into your account*****')
    #Name = first_name + last_name
    accountNumberFromUser = int(input('Accont Number: \n'))
    password = input('Enter your password: \n')
    for accountNumber, userDetails in database.items():
        if accountNumber == accountNumberFromUser:
            if userDetails[4]== password:
                print('Welcome')
                bankOperation(userDetails)
        else:
            print('invalid Account Number or password')
            login()


#perform bank operations
def bankOperation(userDetails):
    options = int(input("What would you like to do?\n (1) deposit\n (2) withdrawal\n (3) logout \n"))

    if options == 1:

        deposit_operation()
    elif options == 2:

        withdrawal_operation()

    elif options == 3:
        logout()
    else:

        print("Invalid option selected")
        bankOperation(userDetails)


def withdrawal_operation():
    print("withdrawal")
    # get current balance
    current_balance = get_current_balance(balance)
    # get amount to withdraw
    withdraw_amount = int(input('How much do you want to withdraw: '))
    if current_balance > withdraw_amount:
        print('Transaction in progress\n please wait!!!')
    else:
        print('Insufficient funds')
    #display current balance
    check_balance = int(input('Do you want to check your balance?\n (1) yes \n (2)no\n '))
    if check_balance == 1:
        active_amt = current_balance - withdraw_amount
        print('Your balance is ', active_amt)
    else:
        logout()



def deposit_operation():
    print("Deposit Operations")
    # get current balance
    current_balance = get_current_balance(balance)
    # get amount to deposit
    deposit_amount = int(input('How much do you want to deposit: '))
    # display current balance
    active_amnt = current_balance + deposit_amount
    print ('Your balance is ', active_amnt)





def logout():
    login()





#generate account number
def generateAccountNumber():
    print('generating account number...')
    print('loading...')
    return random.randrange(111111111,999999999)

# current balance
def get_current_balance(userDetails):
    return userDetails[4]

#def checkBalance():
    #current_balance = get_current_balance(balance)
    
    

init()

