#   SurfaceAreaOfASpherePE1.py
#   A program to compute the surface area and volume of a sphere
#   by: Matthew Wilde
#   9-25-2020

import math

def main():
    sphRad = eval(input("Enter the radius of the sphere "))
    pi = math.pi
    v = 4 / 3 * pi * (sphRad**3)
    a = 4 * pi * (sphRad **2)
    print("The volume is ", v)
    print("The area is ", a)
    
main()
