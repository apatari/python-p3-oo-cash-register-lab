#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0.0
    self.items = []
    

  def add_item(self, str, price, quantity = 1):
    for i in range(quantity):
      self.items.append(str)
    self.total += price * quantity
    self.last = {
      "name": str,
      "price": price,
      "quantity": quantity,
    }

  def void_last_transaction(self):
    if self.last:
      for i in range(self.last["quantity"]):
        self.items.remove(self.last["name"])
      self.total -= self.last["price"] * self.last["quantity"]
      self.last = False

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total -= self.discount * self.total / 100
      report_val = self.total
      if report_val % 1 == 0:
        report_val = int(report_val)
      print(f"After the discount, the total comes to ${report_val}.")
  

