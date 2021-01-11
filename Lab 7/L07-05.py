#   paymentpgrm.py
#   File name: L07-04
#   Description: A program that grades quizs on a 90-100 scale
#   By: Matthew Wilde
#   10-27-2020

import math

def bmiC(weight, height):

    bmi = ((weight * 720) / ((height * 12))**2 )
    print("Your BMI is:",bmi)
    
    if bmi > 25:
        return("Not Healthy")
    elif bmi >= 19 :
        return("Healthy")
    elif bmi < 19:
        return("Not Healthy")
   
    

def main():
    
    uWeight = eval(input("How much do you weigh in pounds: "))
    uHeight = eval(input("How tall are you in feet: "))

    w = bmiC(uWeight, uHeight)

    print("Your BMI is:", w)


main()

