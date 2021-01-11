#   distanceBetweenPE7.py
#   A program that calcualtes the distance between two points 
#   by: Matthew Wilde

import math

def main():
    x1 = eval(input("What is the first x cordinate "))
    y1 = eval(input("What is the first y cordinate "))
    x2 = eval(input("What is the second x cordinate "))
    y2 = eval(input("What is the second y cordinate "))
    distance = ((x2 - x1)**2)+((y2 - y1)**2)
    print("The distance between the two points is ", distance)
    
main()
