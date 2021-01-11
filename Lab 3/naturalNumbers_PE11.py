#   naturalNumbersPE11.py
#   A program that finds the sum of the first n natural numbers, where the
#   value of n is provided by the user. 
#   by: Matthew Wilde
#   09-25-2020
import math

def main():
    n = eval(input("What is the value of n "))
    num1 = 0
    while (n > 0):
        num1=num1+n
        n=n-1
    print ("The sum of first nautral numbes is ", num1)    
main()
