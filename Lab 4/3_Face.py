#   FacePE3.py
#   File name: 3_Face
#   A program that creates a face
#   by: Matthew Wilde
#   9-31-2020


from graphics import *

def main():
    # 100 * 3
    win = GraphWin("Input",600,600)
    face_cir = Circle(Point(300,100),100)
    face_cir.setFill("yellow")
    face_cir.setOutline("black")
    face_cir.draw(win)

    eye1_cir = Circle(Point(250,50),10)
    eye1_cir.setFill("black")
    eye1_cir.setOutline("black")
    eye1_cir.draw(win)

    eye2_cir = Circle(Point(350,50),10) #+200
    eye2_cir.setFill("black")
    eye2_cir.setOutline("black")
    eye2_cir.draw(win)

    mouth_cir = Circle(Point(300,120),60)
    mouth_cir.setFill("white")
    mouth_cir.setOutline("black")
    mouth_cir.draw(win)

    mouth_cir2 = Circle(Point(300,100),60)
    mouth_cir2.setFill("yellow")
    mouth_cir2.setOutline("yellow")
    mouth_cir2.draw(win)


    
    
main()

