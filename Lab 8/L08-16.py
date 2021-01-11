#   colorChange.py
#   A program that sets the background color based on the first letter of a color and by hitting escape clears the txt box
#   File: L08-15
#   by: Matthew Wilde   
#   11-19-2020

from graphics import *

def main():
    win= GraphWin("Entry Window", 500, 500)
    win.setCoords(-20,-20,20,20)
    win.setBackground('white')

    textBox = Entry(Point(0, 0),10)
    textBox.setFill('white')
    textBox.draw(win)

    while True:
        key = win.getKey()
        if key == 'Escape':
            textBox.setText('')

        elif key == 'Return':
            color = textBox.getText()
            if color == 'p':
                win.setBackground('pink')
                textBox.setText('')
            if color == 'r':
                win.setBackground('red')
                textBox.setText('')
            if color == 'o':
                win.setBackground('orange')
                textBox.setText('')
            if color == 'y':
                win.setBackground('yellow')
                textBox.setText('')
            if color == 'c':
                win.setBackground('cyan')
                textBox.setText('')
            if color == 'w':
                win.setBackground('white')
                textBox.setText('')
            if color == '':
                break
    win.close()

main() 
