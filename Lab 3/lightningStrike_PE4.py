#   lightningStrikePE4.py
#   A program that determines the distance to a lightning strike based on
#   the time elapsed between the flash and the sound of thunder.
#   by: Matthew Wilde
#   9-25-2020
import math

def main():
    flashTime = eval(input("Enter the amount of time it was between the flash and the sound of thunder "))
    distance = (flashTime / (5820 / 1100))
    print("The lightning is  ", distance, " miles away.")
    
main()
