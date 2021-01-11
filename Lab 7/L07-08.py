#   senate.py
#   File name: L07-08
#   Description: A program that determines if you can be a US senator or not
#   By: Matthew Wilde
#   11-9-2020

def check(age, citizenshipY):
    s = False
    h = False
    
    if citizenshipY  >= 7:
        if age >= 25:
            h = True
        elif age < 25:
            s = False
            
            
    if citizenshipY  >= 9:
        if age >= 30:
            s = True
        elif age < 30:
            s = False

    print("Status of eligibity for the house:", h)
    print("Status of eligibity for the senate:", s)


def main():
    age = int(input("How old are you: "))
    cY = int(input("How many years have you been a US citizen: "))

    c = check(age, cY)
    

main()
