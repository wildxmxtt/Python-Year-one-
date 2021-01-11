#CH04_PE06.py
#A program using textbook provided graphical future value program code
#     modified so user input of principle and apr is through Entry objects.
#John Smith
#09/23/2020
from graphics import *

def main():
    #Introduction
    print("This program plots the growth of a 10-year investment.")

    #Get principal and interest rate
    win1 = GraphWin("Input by user",400,400)
    win1.setBackground("yellow")
    Text (Point(200,20),"Please Enter the initial principal, not to exceed $10,000: ").draw(win1) 
    textEntry = Entry (Point(150,45),25)
    textEntry.draw(win1)
    text1 = Text(Point(200,200), 'Click mouse anywhere in yellow to continue')
    text1.draw(win1)
    text2 = Text(Point(200,215), 'after entering principal')
    text2.draw(win1)
    win1.getMouse()         # click the mouse to signal done entering text
    principal = float(textEntry.getText())

    text1.undraw()
    text2.undraw()

    Text (Point(200,70),"Please Enter the apr in decimal form: ").draw(win1) 
    textEntry = Entry (Point(150,95),25)
    textEntry.draw(win1)
    text1.draw(win1)
    text2 = Text(Point(200,215), 'after entering apr')
    text2.draw(win1)    
    win1.getMouse()         #click the mouse to signal done entering text
    apr = float(textEntry.getText())
    win1.close()

    #Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")                     
    Text (Point(20,230),'  0.0K').draw(win)         
    Text (Point(20,180),'  2.5K').draw(win)        
    Text (Point(20,130),'  5.0K').draw(win)
    Text (Point(20,80),'  7.5K').draw(win)
    Text (Point(20,30),' 10.0K').draw(win)

    #Draw bar for initial principal
    height = principal *.02
    bar = Rectangle(Point(40, 230),Point(65, 230-height))
    bar.setFill("green")                           
    bar.setWidth(2)                                
    bar.draw(win)

    #Draw bars for successive years
    for year in range (1,11):
        #calculate value for the next year
        principal = principal * (1+apr)
        #draw bar for this value
        x11 = year * 25 + 40
        height = principal *.02
        bar = Rectangle(Point(x11, 230),Point(x11+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)     
        bar.draw(win)        

    input("Please Presss <Enter> to Quit")          
    win.close()

main()
