class Bank:
  def bank(self):
    print("Yes Bank")
  def amount(self,amount):
    self.amount = amount
    print("Amount Received :",amount)
  def deposit(self,deposit_amount):
    update_amount = self.amount + deposit_amount
    print("Deposit :",deposit_amount)
    self.update_amount = update_amount
  def withdraw(self,withdraw_amount):
    update_amount = self.update_amount - withdraw_amount
    print("Withdraw :",withdraw_amount)
    self.update_amount = update_amount
  def tax(self,tax_amount):
    update_amount = self.update_amount*tax_amount/100
    print("Tax :",tax_amount)
    self.update_amount = update_amount
  def customer_info(self,name,acc):
    print("----------Output----------")
    print("Name :",name)
    print("Account Number :",acc)
  def Balance(self):
    print("Balance :",self.update_amount)

b = Bank()
b.bank()
b.amount(3000)
b.deposit(200)
b.withdraw(100)
b.tax(18)
b.customer_info("Lakshya Jain","xxxx3402")
b.Balance()