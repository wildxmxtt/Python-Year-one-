#   grade.py
#   File name: L07-18
#   A program that computes a students grade
#   by: Matthew Wilde
#   10-29-2020

import math

def grade(score):
    
    if score > 100:
        return("That is not a valid score ")
    if score < 0:
        return("That is not a valid score ")
    if score >= 90 or score == 100:
        return("A")
    elif score >= 80 :
        return("B")
    elif score >= 70:
        return("C")
    elif score >= 60:
        return("D")
    elif score < 60:
        return("F")
   

def main():
    
    quizGrade = eval(input("What did you get on your quiz (number) "))

    g = grade(quizGrade)

    print("Your grade is:", g)


main()
