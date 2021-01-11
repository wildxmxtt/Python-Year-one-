#   prime.py
#   A program that finds a prime number
#   File: L08-07
#   by: Matthew Wilde   
#   11-16-2020

import math 
def prime(n):
    isPrime = False
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
    
    #pulls from list
    #adds primes together
    #add primes from slot 0-1, then 1-2, then 2-3 ect
    #check if primes == number 
    x = 0
    y = 1
    for i in range(len(primes)):                
        pCheck = int(primes[i + x]) + int(primes[i + y])
        if pCheck == n1:
            print("The numbers,",int(primes[i + x]),"and", int(primes[i + y]), "add up to", n1)
            break
        if i == len(primes):
            print("None of the primes add up to you number :(")
            break
        else:
            x = x + 1
            y = y + 1
        

                
def main():
    evenOrOddCheck = True
    while evenOrOddCheck == True:
        number = int(input("Enter a number: "))
        if number > 1:
            evenOrOddCheck = False
            p = prime(number)
            break
        else:
            print("Not a correct number, number must be even: ")
                
    
main()
