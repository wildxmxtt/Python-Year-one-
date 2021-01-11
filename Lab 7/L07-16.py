#   TargetPE2.py
#   File name: 2_Target
#   A program that creates a virtual target
#   by: Matthew Wilde
#   9-31-2020


from graphics import *
from math import *


def shots(win):
    for i in range (5):
        arrow = win.getMouse()
        x = arrow.getX()
        y = arrow.getY()
        d = sqrt(x ** 2 + y ** 2)

        
        if d < 2:
            score = 9
        elif d < 4:
            score = 7
        elif d < 6:
            score = 5
        elif d < 8:
            score = 3
        elif d < 10:
            score = 1
        else:
            score = 0
        return score
            
        print("Your ",i +1, "shot is", score)


def main():
    #creates window and target
    win = GraphWin("Archery", 500, 500)
    win.setCoords(-12,-12,12,12)

    cir = Circle(Point(0,0), 5)
    cir.setOutline("black")
    cir.setFill("white")
    cir.setWidth(1)
    cir.draw(win)

    cir2 = Circle(Point(0,0), 4)
    cir2.setOutline("black")
    cir2.setFill("red")
    cir2.setWidth(1)
    cir2.draw(win)

    cir3 = Circle(Point(0,0), 3)
    cir3.setOutline("black")
    cir3.setFill("blue")
    cir3.setWidth(1)
    cir3.draw(win)

    cir4 = Circle(Point(0,0), 2)
    cir4.setOutline("white")
    cir4.setFill("black")
    cir4.setWidth(1)
    cir4.draw(win)

    cir5 = Circle(Point(0,0), 1)
    cir5.setOutline("black")
    cir5.setFill("white")
    cir5.setWidth(1)
    cir5.draw(win)

    finalScore = 0 
    for i in range (5):
        s = shots(win)
        finalScore = s + finalScore
        print("The score for shot:", i + 1, " is", s)

    print("The final score is", finalScore)

    
    
    
main()

