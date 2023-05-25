class Bank():
    bank_name="coop-bank"
    deposits=[]
    withdrawals=[]
    loan_balance=0
    depositting={}
    withdrawing={}
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
        # self.balance-amount
        new_balance=self.account_balance-amount
        if(self.account_balance > amount):
            return f"you have withdrawn {amount} and your balance is {new_balance}"
        else:
            return f"insufficient balance"
    def check_balance(self):
        return f"hello {self.account_name} your balance is {self.account_balance}"
    def deposit(self,amount):
         
         self.deposits.append(amount)
         
         self.depositting["amount"]=amount
         self.depositting["narration"]="deposit"
         return self.depositting
    def withdraw(self,amount):
        self.withdrawals.append(amount)
       
        self.withdrawing["amount"]=amount
        self.withdrawing["narration"]="withdrawal"
        return self.withdrawing
    def print_statement(self):
     self.new_list=[]
     for deposit in self.deposits:
         self.new_list.append(deposit)
     for withdraw in self.withdrawals:
         self.new_list.append(withdraw)

     return self.new_list
              
    def loaning(self,amount):    
        item = len(self.deposits)
        item_s = sum(self.deposits)
        limit = item_s*(1/3)
        amount+=(amount)*0.03 
       
        if amount<=100:
            return "Sorry we can't give you this loan, your loan must be more than 100 "
        elif self.loan_balance>0:
            return f"Dear customer you still have a loan of {self.loan}"
        elif item<10:
            return f"Your deposits must be atleast 10"

        elif amount>=limit:
            return f"Dear customer you can't borrow {amount}is higher than a limit of {self.balance}"

        else:
            self.loan_balance+=amount
     
            return f"Dear customer {self.account_name} your loan of ksh{amount} has been granted successfully"
    def loan_repay(self,amount): 
        if amount<self.loan_balance:
            paying = self.loan_balance-amount
            return f"Dear customer you have paid {amount} and your loan balance is {paying}"
        else:
            over_pay = amount-self.loan
            self.balance+=over_pay
            return f"You succesfully completed paying your loan and the over pay is {over_pay} and your new balance is {self.balance}"    
    
    def transfer(self,amount,receiver):
        self.amount=amount
        self.receiver=receiver
        if(amount < self.account_balance):
            self.account_balance-=amount
            customer2.account_balance+=amount
            return customer2.account_balance

   
            
customer1=Bank("loice",234552224,3000,"business")
print(customer1.deposit(400))
print(customer1.deposit(600))
print(customer1.deposits)
print(customer1.withdraw(400))
print(customer1.withdraw(300))
print(customer1.withdrawals)
print(customer1.print_statement())
customer2=Bank("mary",3729893,5000,"personal")
print(customer1.transfer(2000,customer2))
print(customer1.account_balance)
customer1.loaning(300)

    
        
