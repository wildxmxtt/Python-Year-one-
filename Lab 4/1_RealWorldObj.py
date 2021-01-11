#   RealWorldObjPE1.py
#   File name: 1_RealWorldObj
#   A program that draws ten squares on the screen then closes 
#   by: Matthew Wilde
#   9-31-2020


from graphics import *

def main():
    win = GraphWin()
    for i in range (10):
        shape = Rectangle(Point(30,70), Point(70,30))
        shape.setOutline("red")
        shape.draw(win)
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx,dy)
    quitmessage = Text(Point(100,100), "Click again to quit")
    quitmessage.setSize(18)
    quitmessage.setStyle("bold")
    quitmessage.setTextColor("black")
    quitmessage.draw(win)
    win.getMouse()
    win.close()
main()

