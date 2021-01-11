from math import *
from graphics import *

def main():
    win = GraphWin('Rectangle Information',300,300)
    win.setCoords(-100, -100, 100, 100)
    text = Text(Point(0,50), 'Click on two points to draw a rectangle')
    text.setSize(8)
    text.draw(win)

    pt1 = win.getMouse()
    pt1.draw(win)
    pt2 = win.getMouse()
    rectangle = Rectangle(pt1, pt2)
    rectangle.draw(win)

    text.undraw()

    perimeter = round(2(pt2.getX()-pt1.getX())+2(pt2.getY()-pt1.getY()),4)
    area = round((pt2.getX()-pt1.getX())*(pt2.getY()-pt1.getY()),4)

    text = Text(Point(0, 50),'The perimeter of the line is:' + str(perimeter) +
                '\nThe area of the line is:' + str(area))
    text.setSize(8)
    text.draw(win)


main()
