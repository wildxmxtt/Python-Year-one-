#   quizGraderPE2.py
#   File name: L05-02
#   A program that calculates the grade of students based on a numbering scale 1 - 5
#   by: Matthew Wilde
#   10-13-2020

def main():
    quizGrade = eval(input("What did you get on your quiz (number) "))

    if quizGrade == 5:
        print("A")
    elif quizGrade == 4:
        print("B")
    elif quizGrade == 3:
        print("C")
    elif quizGrade == 2:
        print("D")
    elif quizGrade == 1:
        print("F")
    elif quizGrade == 0:
        print("F")
    
main()
