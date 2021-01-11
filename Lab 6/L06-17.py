#   representNum.py
#   File name: L06-14
#   A program that creates a dot and moves it everytime you click on the window 
#   by: Matthew Wilde
#   10-29-2020

from graphics import *

def moveTo(shape, newCenter, win):
        dx = win.getX() - newCenter.getX()
        dy = win.getY() - newCenter.getY()
            
        
        shape.move(dx,dy)
        

def main():
        win = GraphWin()
        for i in range(10):
            p = win.getMouse()
            shape = Circle(p, 3)
            shape.setOutline("red")
            c = win.getMouse()
            
            shape.draw(win)
        
            moveTo(shape, c, p)
            
        quitmessage.draw(win)
        win.close()

main()
