# Encapsulation

class Bank:
  def __init__(self,bankname,acc_no,balance):
    self.bankname = bankname
    self.acc_no = acc_no
    self.balance = balance

  def get_BankName(self):
    return self.bankname

  def get_Acc_no(self):
      return self.acc_no

  # Getter Method for balance
  def get_Balance(self): 
    return self.balance

  # Setter Method for balance
  def set_balance(self,balance):
    self.balance = balance

b = Bank("Yes Bank",344201000003214,100000)
print(f'Bank Name: {b.get_BankName()}')
print(f'Account Number: {b.get_Acc_no()}')
b.set_balance(30000)
print(f'Balance: {b.get_Balance()}')

