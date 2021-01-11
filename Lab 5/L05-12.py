#   futval.py
#   A program to compute the value of an investment
#   carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a 10 year investment.")
    investTime = eval(input("Enter how long you will be investing for: "))
    investTime = investTime + 1
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    addition = eval(input("How much will be invested each year: "))

    print("Year", "\t", "Value")
    print("------------------")
    
    for i in range(investTime):
        principal += addition
        principal = principal * (1 + apr)
        print(i, "\t" , "$", (round(principal, 2)))
        
    
main()


