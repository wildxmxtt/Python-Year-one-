#   paymentpgrm.py
#   File name: L07-04
#   Description: A program that grades quizs on a 90-100 scale
#   By: Matthew Wilde
#   10-27-2020

def credits(credAmount):
    
    if credAmount >= 26:
        return("Senior")
    elif credAmount >= 16 :
        return("Junior")
    elif credAmount >= 7:
        return("Sophmore")
    elif credAmount < 7:
        return("Freshmen")
    

def main():
    
    creditAmount = eval(input("How many credits do you have: "))

    c = credits(creditAmount)

    print("Your grade is:", c)


main()

