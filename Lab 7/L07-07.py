#   babySitter.py
#   File name: L07-07
#   Description: A program that calculates babysitter rates
#   By: Matthew Wilde
#   11-9-2020
#   Note: 10 to 10 should cost: $29.25
import math  

def calculate(startT, startM, endT, endM):
    hoursWorked = abs(((startT + startM) - (endT + endM))/100)
    bedTP = 0
    totalP = 0
    regP = 0 
    
    regP = hoursWorked * 2.50
    #finds the bed time pay
    
    if endT >= 2100:
        decP = int((endT - 2100) / 100)
        for i in range(decP):
            bedTP = bedTP + (decP * 0.75)
        
                
    #adjust the rate for the regular pay by subtracting the bedtime rate
    totalP = round(regP - bedTP, 2)

    return totalP
    

def main():
    print("Enter the hours you worked in millitarty time")
    startH = int(input("What is the starting hour: "))
    startM = int(input("What is the starting minute: "))
    endH = int(input("What is the ending hour: "))
    endM = int(input("What is the ending minute: "))

    c = calculate(startH,startM, endH, endM)

    print("The price of the baby sitter is $", c)

main()
