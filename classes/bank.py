class Bank():
    bank_name="coop-bank"
    def __init__(self,account_name,account_number,account_balance,account_type) :
        self.account_name=account_name
        self.account_number=account_number
        self.account_balance=account_balance
        self.account_type=account_type
    def account_details(self):
        return f"{self.account_name} accont number{self.account_number} has {self.account_type} account"
    def balance(self,deposit):
        balance=self.account_balance+ deposit
        return balance
# account balance after withdrawal
    def withdraw(self,amount):
        new_balance=self.account_balance-amount
        if(self.account_balance > amount):
            return f"you have withdrawn {amount} and your balance is {new_balance}"
        else:
            return f"insufficient balance"
    
        
