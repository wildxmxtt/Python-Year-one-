#   GCD.py
#   A program that finds the GCD of a number
#   File: L08-07
#   by: Matthew Wilde   
#   11-16-2020

def gdc(a,b):
    if b == 0:
        return a
    else: return gdc(b, a%b)

def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("GDC", gdc(a,b))

main()
