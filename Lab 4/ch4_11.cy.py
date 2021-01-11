from graphics import *
import math
def main():
    win = GraphWin("", 300, 300, False)
    win.setCoords(0.0, 0.0, 10.0, 10.0) 
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    rect = Rectangle(Point(p1.getX(),p1.getY()), Point(p2.getX(),p2.getY()))  
    rect.draw(win) 
    diff = p2.getX() - p1.getX()  
    doorwidth = diff/5  
    hdoorw = doorwidth/2   
    p3 = win.getMouse() 
    p3.draw(win)
    p3_x = p3.getX() 
    doorulx = p3_x - hdoorw
    dooruly = p3.getY()
    doorlrx = p3_x + hdoorw
    doorlry = p1.getY()
    rect2 = Rectangle(Point(doorulx,dooruly), Point(doorlrx,doorlry))
    rect2.draw(win)
    p4 = win.getMouse() 
    p4.draw(win)
    rect3 = Rectangle(Point(p4.getX()-hdoorw/2,p4.getY()+hdoorw/2), Point(p4.getX()+hdoorw/2,p4.getY()-hdoorw/2))
    rect3.draw(win)
    p5 = win.getMouse() 
    p5.draw(win)
    triangle = Polygon(Point(p2.getX(),p2.getY()), Point(p5.getX(),p5.getY()), Point(p1.getX(),p2.getY()))
    triangle.draw(win)
    p6 = win.getMouse()
    win.close()
    
main()
