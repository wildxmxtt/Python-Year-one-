#   manualSquareRootsPE17.py
#   A program that computes square roots
#   by: Matthew Wilde
#   09-25-2020

import math

def main(): 
    x = eval(input("What number would you like to square root "))
    guessAmount = eval(input("How many times would you like guess for the square root "))
    for i in range (guessAmount):
        guessAmount = (guessAmount +(x / guessAmount)) / 2
    print( "The REAL answer is! ", math.sqrt(x))
    ans = guessAmount-math.sqrt(x)
    print( "The diffrence between the square root and guess is! ", ans)
    
   
main()
