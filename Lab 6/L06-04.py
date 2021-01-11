#   sumNum.py
#   File name: L06-04
#   Descrption: A program that prints out the sum of the first n natural numbers and the sum of the cubes of the first n natural numbers. 
#   By: Matthew Wilde 10-28-2020


import math 

def sumN(n):
    sSumN = 1
    for factor in range(n,1,-1):
        sSumN =  sSumN + factor
    
    print("The sum of natural nums is",sSumN)
    
def sumNCubes(n):
    cube = 1
    for factor in range(n,1,-1):
        cube = cube + factor ** 3

    print ("The sum of cubes is",cube)
    
def main():

    number = int(input("Enter a number:"))
    
    sumN(number)
    sumNCubes(number)
    
main()
