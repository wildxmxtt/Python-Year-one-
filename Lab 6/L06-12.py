#   acroynm.py
#   File name: L06-12
#   A program that dose acryonyms
#   by: Matthew Wilde
#   10-29-2020

import math

 
def sumList(nums):
    h = 0 
    for i in range(len(nums)):
        h = nums[i] + h
        
    return h

def main():
    nums = []
    x = 0
    runTime = int(input("How many numbers do you want to input: "))
    for i in range(runTime):
        print("Please enter a number: ")
        userInput = int(input(""))
        nums.append(userInput)

    sL = sumList(nums)
    

    print(sL)

main()
