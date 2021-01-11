#   fibNum.py
#   File e: L06-06
#   Descrption: A program that displays the area of a triangle
#   By: Matthew Wilde 10-28-2020

import math

def triArea(a, b, c): 
    s = (a + b + c) / 2
    a = math.sqrt(s*(s-a)*(s-b)*(s-c))

    return a

def main():
    sides = []
    for i in range(3):
        print("What is the lenght of the", i + 1, "side of the triangle ")
        triSides = int(input(""))
        sides.append(triSides)

    tA = triArea(sides[0], sides[1], sides[2])

    print("The triangles area is:", tA)
    
main()
