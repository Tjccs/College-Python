



class Account:
    '''
    A bank account
    '''

    def __init__(self, numb):
        '''
        Creates an account.

        Requires: numb is int greater than zero, the account number.
        Ensures: a new object Account with the number numn.
        '''
        try:
            if numb > 0:
                self.nib = numb
                self.amount = 0
            else:
                print("Account number must be higher than 0")
        except ValueError:
            print("Not a number")

    def withdraw(self, amnt):
        '''
        Withdraws a given amount from the account.

        Requires: amnt is float greater than zero, the amount to
        withdraw.
        Ensures: self.getAmount()==previous self.getAmount() - amnt
        '''
        self.amount = self.getAmount() - amnt


    def deposit(self, amnt):
        '''
        Deposits a given amount into the account.

        Requires: amnt is float greater than zero, the amount to
        deposit.
        Ensures: self.getAmount()==previous self.getAmount() + amnt
        '''
        self.amount = self.getAmount() + amnt



    def getNum(self):
        '''The account number.
        '''
        return self.nib



    def getAmount(self):
        '''The amount in the account.
        '''
        return self.amount


    def accountType(self):
        '''The type of the account.
        '''
        pass

    def __str__(self):
        return "Account number: "+str(self.nib)+" Amount: "+str(self.amount)

    def __eq__(self, other):
        return self.nib == other.nib

    def __lt__(self)
