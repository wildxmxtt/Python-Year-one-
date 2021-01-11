#   bouncingBall.py
#   File name: L07-17
#   A program that creates a bouncing ball
#   by: Matthew Wilde
#   9-31-2020


from graphics import *
from time import sleep

def main():
    win = GraphWin("Ball bouncing",400,200)

    ball = Circle(Point(50,25),5)
    ball.setFill("blue")
    ball.setOutline("green")
    ball.draw(win)

    dx = 1
    dy = 1

    for i in range(50000):
        sleep(.01)
        ball.move(dx,0)
        
        if ball.getP1().getX() == 390:
            dx = -dx
            ball.move(dx,0)
            
        if ball.getP1().getX() == 0:
            dx = 1
            ball.move(dx,0)
            
    win.getMouse()
    win.close()
    
main()
