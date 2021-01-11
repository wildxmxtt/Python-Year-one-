#   quizGrader2PE3.py
#   File name: L05-03
#   A program that grades 100 point exams on the 90 - 100 scale 
#   by: Matthew Wilde
#   10-13-2020

def main():
    quizGrade = eval(input("What did you get on your quiz (number) "))

    if quizGrade >= 90:
        print("A")
    elif quizGrade >= 80 :
        print("B")
    elif quizGrade >= 70:
        print("C")
    elif quizGrade >= 60:
        print("D")
    elif quizGrade < 60:
        print("F")
    
main()
