#   examScoresP5.py
#   File name: L05-015
#   A This programp plots a horizontal bar chart of student exam scores. 
#   by: Matthew Wilde
#   10-13-2020
#   Practice file ext: C:\Users\Mattw\Desktop\Lab14File.txt
from graphics import *

def main():
    fileName = input("Enter file ext: ")
    inFile = open(fileName, "r")
    n = eval(inFile.readline())

    studNames = []
    scores = []

    for i in range(n):
        name, score_str = inFile.readline().split()
        studNames.append(name)
        scores.append(eval(score_str))

    win = GraphWin('Students scores graph')
    win.setCoords(-40, 0, 110, n)
    win.setBackground("white")

    for i in range(n):
        text = Text(Point(-20, n - 0.5 - i), studNames[i])
        text.setSize(12)
        text.draw(win)
        bar = Rectangle(Point(0, n - 0.70 - i), Point(scores[i], n - 0.35 - i))
        bar.draw(win)

    win.getMouse()
    win.close()
    inFile.close()


main()
