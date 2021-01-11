#   gregorianMoonPE8.py
#   A program that calcualtes the value of the Gregorian moon epact
#   by: Matthew Wilde

import math

def main():
    year = eval(input("What is the year "))
    c = year/ 100
    epact = (8 + (c//4)- c + (((8*c) + 13)//25) + 11*(year%19))%30 
    print("The epact is  ", epact)
    
main()
