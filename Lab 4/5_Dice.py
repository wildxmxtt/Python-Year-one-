#   DicePE5.py
#   File name: 5_Dice
#   A program that creates dice
#   by: Matthew Wilde
#   10-5-2020

from graphics import *

def main():
    win = GraphWin('dice',500,100)
    
    win.setCoords(0,0,5,1)
 
    for i in range(5):
        dice = Rectangle(Point(0.1+i,0.1),Point(0.9+i,0.9))
        dice.setFill('red')
        dice.draw(win)
 
    center = Point((0.5),(0.5))
 

    d1 = Circle(center,0.08)
    d1.setFill('white')
    d1.setOutline('white')
    d1.draw(win)
 
 
    d2a = d1.clone()
    d2a.draw(win)
    d2a.move(0.8,0.2)
 
    d2b = d1.clone()
    d2b.draw(win)
    d2b.move(1.2,-0.2)
 

    d3a = d1.clone()
    d3a.draw(win)
    d3a.move(2.0,0.0)
 
    d3b = d1.clone()
    d3b.draw(win)
    d3b.move(2.2,0.2)
 
    d3c = d1.clone()
    d3c.draw(win)
    d3c.move(1.8,-0.2)
 

    d4a = d1.clone()
    d4a.draw(win)
    d4a.move(2.8,-0.2)
 
    d4b = d1.clone()
    d4b.draw(win)
    d4b.move(2.8,0.2)
 
    d4c = d1.clone()
    d4c.draw(win)
    d4c.move(3.2,0.2)
 
    d4d = d1.clone()
    d4d.draw(win)
    d4d.move(3.2,-0.2)
 

    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(4.0,0.0)
 
    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(3.8,-0.2)
 
    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(3.8,0.2)
 
    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(4.2,0.2)
 
    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(4.2,-0.2)
 
    win.getMouse() 
    win.close()
 
main()
