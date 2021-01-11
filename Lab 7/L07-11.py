#   leapYear.py
#   File name: L07-11
#   Description: A program that calculates whether a year is a leap year. 
#   By: Matthew Wilde
#   11-9-2020

def leapC(year):
    leap = ("a leap year ")
    
    if(year %4) != 0:
        leap = ("not a leap year ")
    else:
        if(year % 100) == 0:
            if (year % 400) == 0:
                leap = ("not a leap year ")
        
    return leap

def main():
    year = int(input("What is the year you want to analyze: "))

    l = leapC(year)

    print("The year is", l)
    
main()
