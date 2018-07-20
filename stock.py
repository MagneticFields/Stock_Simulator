# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:44:10 2018

@author: Alper
"""
buy_bids = []
valid_inputs =['1', '2']
print("Welcome to the simple stock sim program\n")
print("1 for creating a stock\n")
print("2 for creating a trader\n")
response = ('please enter your choice: ')
def create_stock():
    """this little function asks arguments needed by the stock class and crease an instance
        with those arguments"""
    name = input('Please enter the name of the stock: ')
    price = input('please enter the initial price of the stock: ')
    price_flt = float(price)
    lot = input('please indicate how many stocks will be circulating: ')
    lot_int = int(lot)
    name = stock(name, price_flt, lot_int)

while response not in valid_inputs: # program asks user to enter a valid option
    print('that is not a valid input. please try again')
    response = input('please enteryour choice: ')
if response == '1':
    create_stock()

class stock(object):
    """ this is a stock object. It takes name, price and total number 
    stocks as an argument and creates an object with that name
        name = string
        price = float
        lot = integer"""

    def __init__(self, name, price, lot):
        self.name = name
        self.price = price
        self.lot = lot

    def get_name(self):
        return self.name

    def get_price(self):
        """Returns the price of the stock"""
        return self.price

    def get_lot(self):
        return self.lot

    def __str__(self):
        return "Current price of " + self.name + " is " + str(self.price)


class trader(object):
    """Creates a trader  object who buys and sells stocks"""

    def __init__(self, name, portfolio, balance):
        self.name = name
        self.portfolio = portfolio
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name


## The code below should be made with fınctions. I am keeping the 
# object code for future reference
class buy_bid(object):
    def __init__(self, stock, trader, price, amount):
        self.stock = stock
        self.trader = trader
        self.price = price
        self.amount = amount
        if self.amount * self.price > trader.get_balance():
            print("insufficient funds")
        elif stock.get_lot() < amount:
            print('There are not enough stocks')
        else:
            buy_bids.append([stock.get_name(), trader.get_name(), price, amount])

# def buy_bid(stock, trader, price, amount):
#    if trader.get_balance() < price * amount:
#        print('You have insufficient funds')
#    elif stock.get_lot() < amount:
#        print('There is not enough stock to buy')
#    else:
#        buy_bids.append([stock, trader, price, amount])
#    print('Your request has been recorded')
# def show_buys():
#    print(buy_bids)
