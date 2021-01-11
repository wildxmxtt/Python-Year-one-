#   representNum.py
#   File name: L06-13
#   A program that strList is a list of strings, each of which represents a number. Modifies each entry in the list by converting it to a number. 
#   by: Matthew Wilde
#   10-29-2020

import math

def toNumbers (strList):
    finStr = []
    strList = strList.lower()
    strList = strList.replace(" ", '')
    
    
    #takes each letter and adds them to zero, we subtract 96 from the ASCII value
    for i in range (len(strList)):
        finStr.append(ord(strList[i])- 96)


    return(finStr)

    
 
def main():
    uInput = input("What letters do you want to turn into numbers: ")  
    tN = toNumbers(uInput)
    print("The numer vaules are: ", tN)
    

main()
