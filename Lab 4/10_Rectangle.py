#   trianglePE10.py
#   File name: 10_Triangle
#   A program that creates a triangle 
#   by: Matthew Wilde
#   10/09/2020
from graphics import *
import math

def main():
    #Introduction
    print("The user enters three vertices of triangle on the screen.")
    print("The program draws the triangle and computes the perimete and area.")

    #Create graphic window for input
    win = GraphWin("Input by user",600,600)
    win.setCoords(0, 0, 10, 10)
    message = Text(Point(5,9.5),'Click on three points of the triangle vertices in this graphics area.')
    message.draw(win)

    #Get triangle vertices
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    Text(Point(1,4),'Vertices1 x =').draw(win)
    Text(Point(3.1,4),p1.getX()).draw(win)
    Text(Point(6,4),'Vertices1 y = ').draw(win)
    Text(Point(8.1,4),p1.getY()).draw(win)
    Text(Point(1,3.75),'Vertices2 x =').draw(win)
    Text(Point(3.1,3.75),p2.getX()).draw(win)
    Text(Point(6,3.75),'Vertices2 y = ').draw(win)
    Text(Point(8.1,3.75),p2.getY()).draw(win)
    Text(Point(1,3.5),'Vertices3 x =').draw(win)
    Text(Point(3.1,3.5),p3.getX()).draw(win)
    Text(Point(6,3.5),'Vertices3 y = ').draw(win)
    Text(Point(8.1,3.5),p3.getY()).draw(win) 

    #Draw the triangle
    Polygon(p1,p2,p3).draw(win)
    #Compute change in x and y
    dx1 = p2.getX() - p1.getX()
    dy1 = p2.getY() - p1.getY()
    dx2 = p3.getX() - p2.getX()
    dy2 = p3.getY() - p2.getY()
    dx3 = p1.getX() - p3.getX()
    dy3 = p1.getY() - p3.getY()
    #Side Lengths
    aLength = math.sqrt(dx1**2+dy1**2)
    Text(Point(1,3),'The length of a is').draw(win)
    Text(Point(3.5,3),aLength).draw(win)
    bLength = math.sqrt(dx2**2+dy2**2)
    Text(Point(1,2.75),'The length of b is').draw(win)
    Text(Point(3.5,2.75),bLength).draw(win)
    cLength = math.sqrt(dx3**2+dy3**2)
    Text(Point(1,2.5),'The length of c is').draw(win)
    Text(Point(3.5,2.5),cLength).draw(win)
    #Perimeter
    Text(Point(1.45,2.25),'The triangle perimeter is').draw(win)
    Text(Point(4.2,2.25),aLength+bLength+cLength).draw(win)
    #Area
    s=(aLength+bLength+cLength)/2
    area=math.sqrt(s*(s-aLength)*(s-bLength)*(s-cLength))
    Text(Point(1.15,2),'The triangle area is').draw(win)
    Text(Point(3.7,2),area).draw(win)

    input("Please Presss <Enter> to Quit")          
    win.close()
main()

