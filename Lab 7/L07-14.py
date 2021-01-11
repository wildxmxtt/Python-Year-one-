#   CircleIntPE7.py
#   File name: 7_CircleInt
#   A program that omputes the intersection of a circle with a horizontal line and displays the information textually and graphically.
#   by: Matthew Wilde
#   10/01/2020

from math import * 

from graphics import *

def main():

    radius = eval(input("Enter the radius of the circle: "))
    yint = eval(input("Enter the y-intercept of the line: "))

    if radius < yint:
        print("The line does not intersect.")
    else:
        win = GraphWin('Circle intersection calculator')
        win.setBackground("white")
        win.setCoords(-10, -10, 10, 10)
        circle = Circle(Point(0,0), radius).draw(win)
        circle.setOutline("blue")
        Line(Point(0,10),Point(0,-10)).draw(win)
        Line(Point(10,0),Point(-10,0)).draw(win)

        yintLine = Line(Point(10,yint),Point(-10,yint)).draw(win)
        yintLine.setOutline("green")

        xint1 = round((-sqrt(radius2 - yint2)),4)
        xint2 = round((sqrt(radius2 - yint2)),4)

        int1 = Circle(Point(xint1, yint), 0.2)
        int1.setFill('red')
        int1.draw(win)
        int2 = Circle(Point(xint2, yint), 0.2)
        int2.setFill('red')
        int2.draw(win)

        int_info = Text(Point(0, 8), 'X values of points of intersections:\n'+ str(xint1)+ ', ' + str(xint2))
        int_info.setSize(10)
        int_info.draw(win)

main()
