#   prime.py
#   A program that finds a prime number
#   File: L08-06
#   by: Matthew Wilde   
#   11-16-2020

import math 
def prime(n):
    primes = []
    n1 = n
    for i in range(n1):
        n = n - 1
        if n <= n1:
            for i in range(2,n):
               if (n % i) == 0:
                   break
               else:
                   primes.append(n)
                   break 
    return primes
                




def main():
    number = int(input("Enter a number: "))

    p = prime(number)

    print("All the primes are: ", p)
            
    
main()

    
