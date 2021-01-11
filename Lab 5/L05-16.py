#   examScoresP5.py
#   File name: L05-016
#   A This programp plots a horizontal bar chart of student exam scores. 
#   by: Matthew Wilde
#   10-13-2020
#   Practice file ext: C:\Users\Mattw\Desktop\Lab16File.txt
from graphics import *

def main():
    fileName = input("Enter file ext: ")
    inFile = open(fileName, "r")
    num_str = inFile.readline()
    

    count = [0]*11
    for num in num_str:
        count[eval(num_str)] += 1
        

    win = GraphWin('Students scores graph')
    win.setCoords(-10, -10, 100, 120)
    win.setBackground("white")

    for i in range (11):
        text = Text(Point(-5 + i*10, -5), str(i))
        text.setSize(12)
        text.draw(win)
        height = count[i] * 100 / max(count)
        if count != 0:
            bar = Rectangle(Point(-7.5 + i*10, 0), Point(-2.5 + i*10, height))
            bar.draw(win)

    win.getMouse()
    win.close()
    inFile.close()

main()
