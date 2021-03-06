#   TargetPE2.py
#   File name: 2_Target
#   A program that creates a virtual target
#   by: Matthew Wilde
#   9-31-2020


from graphics import *

def main():
    win = GraphWin()
    yell_cir = Circle(Point(100,100),100)
    yell_cir.setFill("yellow")
    yell_cir.setOutline("yellow")
    yell_cir.draw(win)

    red_cir = Circle(Point(100,100),80)
    red_cir.setFill("red")
    red_cir.setOutline("red")
    red_cir.draw(win)

    blu_cir = Circle(Point(100,100),60)
    blu_cir.setFill("blue")
    blu_cir.setOutline("blue")
    blu_cir.draw(win)

    blk_cir = Circle(Point(100,100),40)
    blk_cir.setFill("black")
    blk_cir.setOutline("black")
    blk_cir.draw(win)

    whi_cir = Circle(Point(100,100),20)
    whi_cir.setFill("white")
    whi_cir.setOutline("white")
    whi_cir.draw(win)
    
    
main()

