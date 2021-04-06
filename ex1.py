name = input ('What is your name?:\n ')
allowedNames =('Mercy', 'Grace', 'Deborah', 'Ella', 'Tolu')
allowedPassword = ('babyM', 'Ggirl', 'DDlove', 'sweetE', 'meRcy')

if name in allowedNames: 
    password = input('Enter your password: \n')
    user_id = allowedNames.index(name)
    if password == allowedPassword[user_id]:
        import datetime
        now = datetime.datetime.now()
        print('Date:      Time:')
        print(now.strftime('%Y-%m-%d   %H:%M:%S'))
        
        print ('welcome ' + name)
        print('Options:')
        print('1. Withdraw')
        print('2. Deposit')
        print('3. complaint')
        selectOption = int(input('please select an option: \n'))
        if selectOption == 1:
            
            input('How much would you like to withdraw? \n')
            print('Take your cash')
        elif selectOption == 2:
            input('How much would you like to deposit? \n')
            print('current balance = #####')
        elif selectOption == 3:
            input('What issue will you like to report? \n')
            print('Thank you for contacting us')
        else :
            print('please select an option')

    else:
        print('incorrect password!!!')
else:
    print ('try again')


