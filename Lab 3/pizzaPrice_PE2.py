#   pizzaPricePE2.py
#   A program to compute the cost per square inch of a pizza 
#   by: Matthew Wilde
#   9-25-2020

import math

def main():
    diamiter = eval(input("Enter the diamiter of the pizza "))
    pi = math.pi
    a = pi * ((diamiter/ 2)**2)
    print("The cost per square inch is ", a)
    
main()
