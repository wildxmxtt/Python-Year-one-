#   rLine.py
#   A program that caluates daily cooling a heating days
#   File: L08-13
#   by: Matthew Wilde   
#   11-19-2020
from math import *

from graphics import *

def main():
    pointGet = True
    win = GraphWin("Input by user",600,600)
    win.setCoords(0, 0, 10, 10)
    message = Text(Point(5,9.5),'Click to add points in the graphics area to create a best fit line.')
    message2 = Text(Point(5, 8.5), 'Click square to stop sending points')
    message.draw(win)
    message2.draw(win)
    

    doneBox = Rectangle(Point(-9.75, -9.75), Point(-8.75, -8.75))
    doneBox.draw(win)
    doneText = Text(Point(-9.25,-9.25), "Done")
    doneText.setSize(5)
    doneText.draw(win)

    
    box2=Rectangle(Point(0,0),Point(2,1))
    box2.setFill('red')
    box2.draw(win)


    xPoints = []
    yPoints = []
    xTotal = 0
    yTotal = 0
    h = 0
    x = 0
    y = 0
    xiyi = 0
    xSq = 0
    
    while pointGet == True:
        p = win.getMouse()
        px = p.getX()
        py = p.getY()
        p.draw(win)

        print("x point is", px)
        print("y point is", py)

        xPoints.append(px)
        yPoints.append(py)

        if (px < 2) and (py < 2):   
            pointGet = False
            
            
            for i in range(len(xPoints)):
                xTotal = int(xPoints[h]) + xTotal
                yTotal = int(yPoints[h]) + yTotal
                h = h + 1
                xiyi += px * py
                xSq += px**2
            

            xAvg = xTotal / (int(len(xPoints)))
            yAvg = yTotal / (int(len(yPoints)))

            m = (xiyi - (len(xPoints) * yAvg * xAvg))/(xSq - (len(xPoints) * xAvg**2))

            lP = Point(-10, (yAvg + (m * (-10 - xAvg))))
            rP = Point(10, (yAvg + (m * (10 - xAvg))))

            line = Line(lP, rP)
            line.draw(win)
    
main()
