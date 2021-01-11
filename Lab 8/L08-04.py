#   sauce.py
#   A program that uses the Syracuse sequence
#   File: L08-03
#   by: Matthew Wilde   
#   11-16-2020
import math
def syr(x):
    while x > 1:
        if (x % 2) == 0:
            x = x / 2
            print(x)
        else:
            x = (3 * x) + 1
            print (x) 

def main():
    startingNumber = eval(input("What is the number you want to start with: "))

    print(startingNumber)
    sauce = syr(startingNumber)

    
main()
