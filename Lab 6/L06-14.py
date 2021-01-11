#   representNum.py
#   File name: L06-14
#   A program that strList is a list of strings, each of which represents a number. Modifies each entry in the list by converting it to a number. 
#   by: Matthew Wilde
#   10-29-2020
#   Practice file ext: C:\Users\Mattw\Desktop\L5_14File.txt

import math


def sumList(nums):
    h = 0 
    for i in range(len(nums)):
        h = int(nums[i]) + h
        
    return h


def squareEach(nums):
    h = 0
    m = []
    for i in range(len(nums)):
        h = int(nums[i]) **2    
        m.append(h)

    #print("Squared nums: ", m)
    return m 


def main():
    fileExt = input("What is the file extention for a file you want to analyize ")
    content = open(fileExt, "r")
    content = (content.read())
    #Makes a list and splits the numbers up everytime there is a space
    content = content.split()
    
    

    sE = squareEach(content)
    sL = sumList(content)
    

    print("The sum of all numbers is: ", sL, "\n All numbers squared is:",sum(sE))
     


main()
