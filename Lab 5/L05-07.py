#   ceasearCipherP5.py
#   File name: L05-07
#   A program that turns a users input into an encrypted cypher
#   by: Matthew Wilde
#   10-13-2020





def main():
    finStr = ""
    
    #Takes input from the user 
    message = input("What is the message you want to encrypt? ")
    message = message.lower()
    
    
    
    
    #takes each letter and adds them to zero, we subtract 96 from the ASCII value
    for i in range (len(message)):
        finStr = finStr + chr((ord(message[i])) + 2)
        

    print(finStr)
    
main()
