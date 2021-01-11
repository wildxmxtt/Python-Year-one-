#   invest.py
#   A program that invests.
#   File: L08-03
#   by: Matthew Wilde   
#   11-16-2020

def main():
    aR = eval(input("What is the Anualized intrest rate: "))
    iV = eval(input("What is the inital investment: "))
    
    doubled = iV * 2
    years = 0
    while iV < doubled:
        iV = iV * aR
        years = years + 1
    print ("The amount of years it would take is: ", years)
        
        
main()
