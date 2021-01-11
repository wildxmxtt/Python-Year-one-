#   leapYear.py
#   File name: L07-12
#   Description: A program that accepts calander dates
#   By: Matthew Wilde
#   11-9-2020

def dateValid(month, day, year):
    leap = True

    if (year % 4) != 0:
        leap = False
    else:
        if (year % 100) == 0:
            if (year % 400) ==0:
                leap = False



    if month > 12 or day > 31:
        print("This date is invalid.")
    else:
        if day <= 28:
            print("This date is valid.")
        elif month == 2 and day == 29:
            if leap == False:
                print("This date is invalid.")
            else:
                print("This date is valid.")
        elif day == 31:
            if month == 2 or 4 or 6 or 11:
                print("This date is invalid")
            else:
                print("This date is valid")
        else:
            print("The date is valid.")





def main():
    dateStr = input("Enter a date (month/day/year) ")

    monthStr, dayStr, yearStr = dateStr.split("/")
    month = int(monthStr)
    day = int(dayStr)
    year = int(yearStr)

    d = dateValid(month, day, year)

main()
