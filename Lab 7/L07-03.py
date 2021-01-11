#   paymentpgrm.py
#   File name: L07-03
#   Description: A program that grades quizs on a 90-100 scale
#   By: Matthew Wilde
#   10-27-2020


def grade(score):
    
    if score >= 90:
        return("A")
    elif score >= 80:
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
