#   prime.py
#   A program that finds a prime number
#   File: L08-05
#   by: Matthew Wilde   
#   11-16-2020

def prime(n):
    if n > 1:
        for i in range(2,n):
           if (n % i) == 0:
               print(n,"is not a prime number")
               break 
           else:
               print(n,"is a prime number")
               break 
        



def main():
    number = int(input("Enter a number: "))

    p = prime(number)

    
    
    
    
main()
