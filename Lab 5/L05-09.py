#   wordCounterP5.py
#   File name: L05-09
#   A program that counts the amount of words in a sentence entered by a user.
#   by: Matthew Wilde
#   10-13-2020





def main():
    
    #Takes input from the user 
    content_sentence = input("Enter a sentence ")
    
    split = len(content_sentence.split()) 
    
    print ("The number of words in string are : " +  str(split)) 
    
main()
