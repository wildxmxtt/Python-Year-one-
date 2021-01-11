#   lenghtOfaLadderPE10.py
#   A program that calcualtes the  length of a ladder required to reach a
#   given height when leaned against a house
#   by: Matthew Wilde

import math

def main():
    height = eval(input("What is the height of the ladder "))
    angle = eval(input("What is the angle (in degrees) of the ladder "))
    pi = math.pi
    radians = (pi / 180)*angle
    lenght = height  / (math.sin(radians))
    print("The lenght needed is ", lenght)
    
main()
