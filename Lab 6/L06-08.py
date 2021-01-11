#   guess.py
#   File name: L06-08
#   A program that computes a guess
#   by: Matthew Wilde
#   09-25-2020

import math

def nextGuess(guess, x):
    for i in range (guess):
        guess = (guess +(x / guess)) / 2
    ans = guess-math.sqrt(x)
    

    return ans

def main():
    x = eval(input("What number would you like to square root "))
    guessAmount = eval(input("How many times would you like guess for the square root "))

    nG = nextGuess(guessAmount, x)

    print( "The diffrence between the square root and guess is! ", nG)
    
main()
