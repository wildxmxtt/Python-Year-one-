#   representNum.py
#   File name: L06-14
#   A program that makes a smiley face :)
#   by: Matthew Wilde
#   10-29-2020

from graphics import *

def drawFace(center, size, win):
    x = 0
    h = 0
    for i in range(3): 
        face_cir = Circle(Point(center + x ,center),size)
        face_cir.setFill("yellow")
        face_cir.setOutline("black")
        face_cir.draw(win)

        eye1_cir = Circle(Point(center - 50 + x,center - 50),size - 90)
        eye1_cir.setFill("black")
        eye1_cir.setOutline("black")
        eye1_cir.draw(win)

        eye2_cir = Circle(Point(center + 50 + x ,center - 50),size - 90)
        eye2_cir.setFill("black")
        eye2_cir.setOutline("black")
        eye2_cir.draw(win)

        mouth_cir = Circle(Point(center + x,center + 20),size - 40)
        mouth_cir.setFill("white")
        mouth_cir.setOutline("black")
        mouth_cir.draw(win)

        mouth_cir2 = Circle(Point(center + x,center),size - 40 )
        mouth_cir2.setFill("yellow")
        mouth_cir2.setOutline("yellow")
        mouth_cir2.draw(win)

        x = (x + 200)


def main():
    win = GraphWin("Input by user",600,600)
    centr = 100
    size = 100

    drawFace(centr, size, win)
    


main()
