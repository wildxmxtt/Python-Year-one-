#   ceasearCipher2P5.py
#   File name: L05-08
#   A program that turns a input into an encrypted cypher, can take the full name
#   by: Matthew Wilde
#   10-13-2020





def main():
    finStr = ""
    i = 0
    #Takes input from the user 
    message = input("What is the message you want to encrypt? ")
    message = message.lower()
    
    
    #Takes the message lenght, then test to see if the ASCII value is higher than "z", if it is then it subtracts 26 to go back to ASCII value "a" 
    for i in range (len(message)):
        #Takes each letter and adds them to zero, then adds 2. Ex. if "a" is entered it would print "c" because "c" is two postions higher than "a" 
        finMessage = chr((ord(message[i])) + 2)
        
        if (ord(finMessage)) >= 122:
            finMessage = chr((ord(finMessage) - 28))
        
            
     #Combines eacher letter inputed into a final message        
        finStr = finStr + finMessage
    
        
        
#Prints the result
    print(finStr)
  
    
main()
