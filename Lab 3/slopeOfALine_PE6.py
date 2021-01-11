#   slopeOfALinePE6.py
#   A program that determines the slope of a line 
#   by: Matthew Wilde

import math

def main():
    x1 = eval(input("What is the first x cordinate "))
    y1 = eval(input("What is the first y cordinate "))
    x2 = eval(input("What is the second x cordinate "))
    y2 = eval(input("What is the second y cordinate "))
    slope = ((y2 - y1)/(x2 - x1))
    print("The slope of the line is ", slope)
    
main()
