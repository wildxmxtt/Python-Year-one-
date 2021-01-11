#   representNum.py
#   File name: L06-16
#   A program that puts a cartoon face on a face
#   by: Matthew Wilde
#   10-29-2020
#   Pratice File Ext: C:\Users\Mattw\Desktop\Froze_Cam background.PNG

from graphics import *

def drawFace(center, size, win):
        x1 = center.getX()
        y1 = center.getY()
        
        
        face_cir = Circle(Point(x1,y1),size + 1)
        face_cir.setFill("yellow")
        face_cir.setOutline("black")
        face_cir.draw(win)

        eye1_cir = Circle(Point(x1 - 1 * 0.7 ,y1 + 2),size * 0.15)
        eye1_cir.setFill("black")
        eye1_cir.setOutline("black")
        eye1_cir.draw(win)

        eye2_cir = Circle(Point(x1 + 1 * 0.7,y1 + 2),size * 0.15)
        eye2_cir.setFill("black")
        eye2_cir.setOutline("black")
        eye2_cir.draw(win)

        mouth_cir = Circle(Point(x1,y1 - 2),size * 0.60)
        mouth_cir.setFill("white")
        mouth_cir.setOutline("black")
        mouth_cir.draw(win)

        





def main():
    fileExt = input("What is the file extention for a file you want to analyize ")
    
    n = eval(input("How many faces should we block? "))
    img = Image(Point(10, 10), fileExt)
    imgWidth = img.getWidth()
    imgHeight = img.getHeight()

    window = GraphWin('Smile!', imgWidth,imgHeight)
    window.setCoords(0, 0, 20, 20)
    img.draw(window)

   

    for i in range(n):
        point = window.getMouse()
        drawFace(point, 3, window)



main()
