#   voulumeOfSphere.py
#   File name: L06-03
#   Descrption: A program that prints the voulume and area of a sphere
#   By: Matthew Wilde 10-28-2020


import math 

def sphereArea(radius):
    pi = math.pi
    sa = (4 * pi * (radius **2))
    print("The area is ",sa)
    
def sphereVolume (radius):
    pi = math.pi
    v = ((4/3) * pi * (radius **3))
    print("The volume is ", v)
    
def main():
    
    r = int(input("What is the radius: "))
    
    sphereArea(r)
    sphereVolume(r)

main()
