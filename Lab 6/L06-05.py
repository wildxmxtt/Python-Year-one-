#   cubes.py
#   File name: L06-05
#   Descrption: A program that Use two functions-one to compute the area of a pizza, and one to compute cost per square inch. 
#   By: Matthew Wilde 10-28-2020


import math

def sphereArea(radius):
    pi = math.pi
    sa = (4 * pi * (radius **2))

    return sa

def pizzaCost(radius):
    pi = math.pi
    a = (pi * (radius **2))

    
    return a

def main():
    userInput = int(input("What is the radius of the pizza: "))
                
    sphA = sphereArea(userInput)
    pC = pizzaCost(userInput)

    print("The cost per square inch is: $", round(pC, 2), "The area is:", round(sphA, 2), "inches")

main()
