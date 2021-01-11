#   fibonacciSequence.py
#   A program that replactes the fibbonaci sequence of this series
#   File: L08-01
#   by: Matthew Wilde   
#   09-25-2020

import math

def main(): 
    runTime = eval(input("How many numbers are to be summed "))
    j = 1
    k = 0
    fib = 0
    for i in range (runTime):
        fib = j + k
        j = k
        k = fib
    print(fib)
   
main()
