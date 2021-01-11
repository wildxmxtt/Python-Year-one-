#   acronymPE4.py
#   File name: L05-04
#   A program that creates acronyms out of words
#   by: Matthew Wilde
#   10-13-2020

def main():
    phrase = input("What is a phrase you want to make an acronym ")
    finStr = ""
    words = phrase.split(" ")

    for i in range (len(words)):
        words[i] = words[i].upper()
    
    for i in range (len(words)):
        wordSplit = words[i]
        finStr = finStr + wordSplit[:1]
        
    print(finStr)
    
main()
