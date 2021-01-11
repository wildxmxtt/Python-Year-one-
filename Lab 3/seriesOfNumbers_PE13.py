#   seriesOfNumbersPE13.py
#   A program that sums a series of numbers entered by the user
#   by: Matthew Wilde

import math

def main(): 
    runTime = eval(input("How many numbers are to be summed "))
    h = 0
    for i in range(runTime):
        numbers = eval(input("Enter a number you want to sum "))
        h = h + numbers 
    print ("The sum is ", h)    
main()
