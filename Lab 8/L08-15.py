#   oppositeColor.py
#   A program that sets the colors to their corresponding color negatives
#   File: L08-15
#   by: Matthew Wilde   
#   11-19-2020
#   Practice File extention: C:\Users\Mattw\Desktop\RampMeme.ppm

from graphics import *


def imgWindow(fileExt, iWidth, iHeight):
    win = GraphWin("Color negative", iWidth, iHeight)
    fileExt.draw(win)

    height = 1


    while height < iHeight:
        for i in range (iWidth - 1):
            r, g, b = fileExt.getPixel(i + 1, height)
            brightness = int(round(255 - r + 255 - g + 255 - b))

            fileExt.setPixel((i + 1), (height), color_rgb(brightness, brightness, brightness))
            


        win.update()
        height = height + 1

    return win

def main():
    fileExt = input("What is the file extention for a file you want to analyize ")
    print("The extention is: ", fileExt)
    content = Image(Point(0,0), fileExt)

    iWidth = content.getWidth()
    iHeight = content.getHeight()
    
    content = Image(Point(iWidth/2, iHeight/2), fileExt)

    win = imgWindow(content, iWidth, iHeight)
    
    
main()
