#   coffeeShopPE5.py
#   A program that calculates the cost of orders at the  Konditorei coffee shop
#   by: Matthew Wilde
#   9-25-2020

import math

def main():
    poundsOfCfe = eval(input("How many pounds of coffee did the customer order "))
    orderTotal = ((poundsOfCfe * 10.50) + (poundsOfCfe * 0.86) + 1.50)
    print("The order will cost ", orderTotal)
    
main()
