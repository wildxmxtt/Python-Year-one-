#   rectangleDrawPE9.py
#   File name: 9_Rectangle
#   A program that omputes the intersection of a circle with a horizontal line and displays the information textually and graphically.
#   by: Matthew Wilde
#   10/09/2020

from math import *
from graphics import *

def main():
#Creats window 
    win = GraphWin("Input by user",600,600)
    win.setBackground("white")
    win.setCoords(0, 0, 10, 10)
#Gets mouse Input and creates the rectangle
    pt1 = win.getMouse()
    pt1.draw(win)
    pt2 = win.getMouse()
    rectangle = Rectangle(pt1, pt2)
    rectangle.draw(win)


    perimeter = round(2(pt2.getX()-pt1.getX())+2(pt2.getY()-pt1.getY()),4)
    area = round((pt2.getX()-pt1.getX())*(pt2.getY()-pt1.getY()),4)

    text = Text(Point(0, 50),'The perimeter of the line is:' + str(perimeter) +
                '\nThe area of the line is:' + str(area))
    text.setSize(8)
    text.draw(win)

    win.getMouse()
    win.close()
    
main()
