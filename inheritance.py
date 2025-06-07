
# Single Inheritance

class Name:
  def name(name):
    print("Name:",name)

class Age(Name):
  def age(age):
    print("Age:",age)

obj = Age
obj.name("Lakshya")
obj.age(19)

# Multilevel Inheritance

class Height(Age):
  def height(height):
    print("Height:",height)

obj1 = Height
obj1.name("Lakshya")
obj1.age(19)
obj1.height(5.11)

# Multiple Inheritance

class Lion:
  def lion_sound():
    print("Roar")

class Elephent:
  def elephent_sound():
    print("Pawoo")

class Animal(Lion,Elephent):
  def animal_sound():
    print("---Animal Sound---")

obj2 = Animal
obj2.animal_sound()
obj2.lion_sound()
obj2.elephent_sound()

# Hierarchical Inheritance

class Customer:
  def customer_info(self,name):
    print("Customer Name:",name)

class Account(Customer):
  def acc_info(self,acc):
    print("Account No.:",acc)

class Bank(Customer):
  def bank_name(self):
    print("---Yes Bank---")

class Amount(Bank):
  def amount(self,amount):
    self.amount = amount
    print("Amount:",amount)

class Deposit(Amount):
  def deposit(self,deposit_amount):
    update_amount = self.amount + deposit_amount
    print("Deposit :",update_amount)
    self.update_amount = update_amount

class Withdraw(Amount):
  def withdraw(self,withdraw_amount):
    update_amount = self.update_amount - withdraw_amount
    print("Withdraw:",update_amount)
    self.update_amount = update_amount

class Balance(Deposit,Withdraw):
  def balance(self):
    print("Balance:",self.update_amount)

class Address(Account,Balance):
  def address(self):
    print("Branch Borivali")

a = Address()
a.bank_name()
a.address()
a.customer_info("Lakshya Jain")
a.acc_info(344201000003214)
a.amount(500)
a.deposit(2000)
a.withdraw(1000)
a.balance()