#   daysOfTheYear.py
#   File name: L07-13
#   Description: A program that prints what day of the year it is
#   By: Matthew Wilde
#   11-9-2020

import math

def leapYear(month, day, year):
    
    leap = True
    dateFormat = True

    if (year % 4) != 0:
        leap = False
    else:
        if (year % 100) == 0:
            if (year % 400) ==0:
                leap = False
                
    print("Leap year is", leap)

    return leap


def dateValid(month, day, year):
    
    if month > 12 or day > 31:
        dateFormat = False
    else:
        if day <= 28:
            dateFormat = True
        elif month == 2 and day == 29:
            if leap == False:
                dateFormat = False
            else:
                dateFormat = True
        elif day == 31:
            if month == 2 or 4 or 6 or 11:
                dateFormat = False
            else:
                dateFormat = True
        else:
            dateFormat = True
            
    return dateFormat

def yearConvert(month, day, year, l):

    dayNum = 31 * (int(month) - 1) + day 

    if month > 2:
        dayNum = dayNum - (4 * (int(month))+23)//10
        if day > 29 and l == True:
            dayNum = dayNum + 1
            
    if month >= 3 and l == True:
        dayNum = dayNum + 1
            
            
    return dayNum
    

def main():
    dateStr = input("Enter a date (month/day/year) ")

    monthStr, dayStr, yearStr = dateStr.split("/")
    month = int(monthStr)
    day = int(dayStr)
    year = int(yearStr)

    d = dateValid(month, day, year)
    l = leapYear(month, day, year)

    if d == True:
        y = yearConvert(month, day, year, l)
        print("The day is", y)
    elif d == False:
        print("Cannot run due to invalid date, try again")
        
    

main()
