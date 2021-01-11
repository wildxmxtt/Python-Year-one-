#   modDateCovnerterPE1.py
#   File name: L05-01
#   A program that prints the date
#   by: Matthew Wilde
#   10-13-2020




def main():
    #get the date
    day, month, year = eval(input("Enter a day, month, and year in numbers: "))

    months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]


    monthStr = months[month-1]



    #prints the out put
    print("The converted date is {1}/{0}/{2}, or {3} {0},{2}".format(day, month, year, monthStr))

main()


