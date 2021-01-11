#   wordCounterP5.py
#   File name: L05-10
#   A program that counts the average word lenght in a sentence entered by a user.
#   by: Matthew Wilde
#   10-13-2020





def main():
    avgWordLenght = 0
    
    #Takes input from the user 
    sentence = input("Enter a sentence ")


    #First part counts the amoutnt of words, the second part counts how many words there are
    avgWordLenght = len(sentence.replace(' ',''))/len(sentence.split())

    print(avgWordLenght)

main()


