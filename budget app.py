import os
def create_spend_chart(categories):
    return none
database = {}
class lifestlye():
    def __init__(self, category, amount):
        os.system('cls')
        self.category = category
        self.amount = amount
        #self.lifestlye= float(input('how much is your budget? \n'))
    def deposting_funds(amount, bal):
        bal += amount
        return bal
    
 
    def withdrawing_funds(user, amount, bal):
        bal -= amount
        return bal

    def balance(db):
        for categ,bal in db.items():
            print (categ,bal)
    

    def transfering_balance_account(db, option1, amount, option2):
        value1 = db[option1]
        value2 = db[option2]

        db[option1] = int(value1) - amount
        db[option2] = int(value2) + amount
        return db
    def init():
        print('===**** Your personal Budget****====\n')
        menu()
    def menu():
        try:
            user = int(input('\nwhat do you want to do?\n1) Create a new budget\n2) Deposite into a Budget\n3) Withdraw from a Budget\n4)check Balance\n5) Make Transaction'))
        except:
            print ('invalid option')
            menu()

         

    

