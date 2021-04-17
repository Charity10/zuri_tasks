import os
class lifestlye():
    def __init__(self):
        os.system('cls')
        #self.category = category
        #self.amount = amount
        self.lifestlye=('Welcome !!!\nYou are one step to start saving wisely')
        self.main()
      #amount = 0
        #for i in amount:
         #amount

    def main(self):
       os.system('cls')
       print(self.lifestlye)
       main_option = int(input('\nwhat do you want to do?\n1) Create a new budget\n2) Deposit into a Budget\n3) Withdraw from a Budget\n4) Check Balance\n5) Make Transaction\n'))
       if main_option == 1:
           self.New_budget()
       elif main_option == 2:
            self.Deposit()
       elif main_option == 3 :
            self.Withdraw()
       elif main_option == 4:
            self.Check_balance()
       elif main_option == 5:
            self.Transaction()
       else:
        quit


    def New_budget(self):
        os.system('cls')
        print('\nCreating a new budget\n')
        budget_title = input('Budget Name: \n')
        budget_amount = input("What's your budgeted amount?: \n $")
        budget_total = print('Your total budget is', budget_amount)
        lifestlye()
        

    def Deposit(self):
        os.system('cls')
        int(input('How much would you like to deposit?: \n$'))
        print('Depositing funds...')
        option= input('Do you want to check your balance?: \n1) Yes \n2) No\n')
        if option == 1:
            Check_balance()
        else:
            B= input('Do you want to perform another transaction?: \n1) Yes \n2) No\n')
            if B == 1:
                lifestlye()
            else:
                quit

    def Withdraw(self):
        os.system('cls')
        int(input('How much would you like to withdraw?: \n$'))
        print('withdrawing funds')
        option= input('Do you want to check your balance?: \n1) Yes \n2) No\n')
        if option == 1:
            Check_balance()
        else:
            C= input('Do you want to perform another transaction?: \n1) Yes \n2) No\n')
            if C == 1:
                lifestlye()
            else:
                quit # I dunno why this code isnt working as expected, i wanted the user to be able to perform other trancstions but the program just ends everytime


    def Check_balance():
        os.system('cls')
        print('checking balance')
        print('your balance is $ ') # I was having troubles in adding amount, i know i got one mark deducted the last time for it

    def Transaction(self):
        os.system('cls')
        trans= print(' Note: you can only transfer twice a day')
        
        input( 'Enter the recieving budget: \n')
        input( 'Enter the sending budget: \n')
        int(input( 'Amount you want to transfer: \n'))
        print('Thanks for your time')


lifestlye()