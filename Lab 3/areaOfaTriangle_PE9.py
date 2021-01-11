#   areaOfaTrianglePE9.py
#   A program that calcualtes the area of a triangle
#   by: Matthew Wilde

import math

def main():
    a = eval(input("give the lenght of a side "))
    b = eval(input("give the lenght of a second side "))
    c = eval(input("give the lenght of third side "))
    s = (a + b + c) / 2
    a = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area of the triangle is  ", a)
    
main()
