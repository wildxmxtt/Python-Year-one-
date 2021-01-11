#   naturalNumbersCubedPE12.py
#   A program that finds the find the sum of the cubes of the first n natural numbers
#   where the value of n is provided by the user
#   by: Matthew Wilde

import math

def main():
    n = eval(input("What is the value of n "))
    num1 = 0
    while (n > 0):
        num1=num1+(n**3)
        n=n-1
    print ("The sum of cubes is ", num1)    
main()
