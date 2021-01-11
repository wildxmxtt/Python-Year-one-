#   lineDrawPE8.py
#   File name: 8_LineDrawing
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
#Gets mouse Input and creates line 
    p1 = win.getMouse()
    p1_x = p1.getX()
    p1_y = p1.getY()
    p1.draw(win)
    p2 = win.getMouse()
    p2_x = p2.getX()
    p2_y = p2.getY()
    p2.draw(win)

    l = Line(p1, p2)
    l.draw(win)
    
    dx = (p2_x) - (p1_x)
    dy = (p2_y) - (p1_y)
    
    if (dx) == 0:
        message3 = Text(Point(-5,6), ("The slope of the line is vertical."))
    else:
        slope = round((dy/dx), 2)
        
    lenght = round(sqrt((dx **2) + (dy**2)), 2)
    
    slope = round(slope, 2)
    
    lenght = round(lenght, 2)
#Prints text 
    text = Text(Point(5,8), "The slope is " + str(slope) + " The lenght is " + str(l))
    text.draw(win)

    text2 = Text(Point(0,0), "Click again to close the program" )
    text2.draw(win)
    win.getMouse()
    
    win.close()

main()
