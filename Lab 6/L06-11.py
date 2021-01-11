#   acroynm.py
#   File name: L06-11
#   A program that dose acryonyms
#   by: Matthew Wilde
#   10-29-2020

import math

def squareEach(nums):
    x = nums **2    

    print("The number squared is", x) 

def main():
    nums = []
    x = 0
    runTime = int(input("How many numbers do you want to input: "))
    for i in range(runTime):
        print("Please enter a number: ")
        userInput = int(input(""))
        nums.append(userInput)

        sE = squareEach(nums[x])
        x = x + 1

    print(sE)

main()

    
