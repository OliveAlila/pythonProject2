# parent/superclass

class Mpesa:
  def __init__(self, account_balance, phone_number):
    self.account_balance = account_balance
    self.phone_number = phone_number

  def send_money(self, amount, recipient):
    if self.account_balance >= amount:
      self.account_balance -= amount
      print(f"{amount} KES sent to {recipient} successfully")
    else:
      print(f"Insufficient balance")


# child classes
class PersonalMpesa(Mpesa):
  def __init__(self, account_balance, phone_number, id_number):
    super().__init__(account_balance, phone_number)
    self.id_number = id_number

  def buy_airtime(self, amount):
    if self.account_balance >= amount:
      self.account_balance -= amount
      print(f"{amount} has successfully been credited")
    else:
      print(f"Insufficient balance")

  # child_class2


class BusinessMpesa:
  def __init__(self, account_balance, phone_number, business_name):
    super().__init__(account_balance, phone_number)
    self.business_name = business_name

  def receive_payment(self, amount, client):
    self.account_balance = + amount
    print(f"{amount} KES received from a {client}")


Personal = PersonalMpesa(1450, 123456789, 1200000)
Personal.send_money(1000, 12356789)
Personal.buy_airtime(100)
# instance for business class
Business = BusinessMpesa(1450, 123456789, "Candy_link")
Business.receive_payment(1000, 123456789)
