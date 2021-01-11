#   paymentpgrm.py
#   File name: L07-02
#   Description: A program that grades quizs on a 1-5 scale
#   By: Matthew Wilde
#   10-27-2020


def grade(score):
    
    if score == 5:
        return("A")
    elif score == 4 :
        return("B")
    elif score == 3:
        return("C")
    elif score == 2:
        return("D")
    elif score == 1:
        return("F")
    

def main():
    
    quizGrade = eval(input("What did you get on your quiz (number) "))

    g = grade(quizGrade)

    print("Your grade is:", g)


main()
