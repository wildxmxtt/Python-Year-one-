#   seriesOfNumberPE15.py
#   A program that  approximates the value of pi by summing the terms
#   of this series
#   by: Matthew Wilde

import math

def main(): 
    runTime = eval(input("How many numbers are to be summed "))
    pi = math.pi
    h = 0
    for i in range(runTime):
        numbers = eval(input("Enter a number you want to sum "))
        h = h + numbers
    k = pi - h
    print ("The sum is ", k)    
main()
