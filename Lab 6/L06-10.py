#   acroynm.py
#   File name: L06-10
#   A program that dose acryonyms
#   by: Matthew Wilde
#   10-29-2020

import math

def acronym(phrase):
    finStr = ""
    words = phrase.split(" ")

    for i in range (len(words)):
        words[i] = words[i].upper()
    
    for i in range (len(words)):
        wordSplit = words[i]
        finStr = finStr + wordSplit[:1]
        
    return(finStr)    



def main():
    inputPhrase = input("What is a phrase you want to make an acronym ")    

    p = acronym(inputPhrase)
    
    print("Your phrase is", p)


main()
