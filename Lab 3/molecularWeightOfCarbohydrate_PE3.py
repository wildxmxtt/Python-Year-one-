#   molecularWeightOfCarbohydratePE3.py
#   A program to computes the molecular weight of a carbohydrate (in
#   grams per mole) based on the number of hydrogen, carbon, and oxygen
#   atoms in the molecule. 
#   by: Matthew Wilde
#   9-25-2020

import math

def main():
    hydroA = eval(input("Enter the number of number of hydrogen atoms "))
    carbA = eval(input("Enter the number of number of carbon atoms "))
    oxeyA = eval(input("Enter the number of number of oxeygen atoms "))
    combinedA = (hydroA *1.00794) + (carbA * 12.0107) + (oxeyA * 15.9994)
    print("The combined weight of the atoms is ", combinedA)
    
main()
