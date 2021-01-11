#   numerologist2P5.py
#   File name: L05-06
#   A program that turns a users name into numbers, can take the full name
#   by: Matthew Wilde
#   10-13-2020





def main():
    finStr = 0
    
    #Takes input from the user 
    name = input("What is your name ")
    name = name.lower()
    name = name.replace(" ", '')
    
    
    #takes each letter and adds them to zero, we subtract 96 from the ASCII value
    for i in range (len(name)):
        finStr = finStr + (ord(name[i])- 96)


    print(finStr)
    
main()
