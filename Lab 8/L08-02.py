#   windChill.py
#   A program that prints a formatted table of windchill values.
#   File: L08-01
#   by: Matthew Wilde   
#   11-16-2020

import math

def windchill(windSpeed, temp):
    w = (35.74 + (0.6215 * (temp)) - (35.75(windSpeed ** 0.16)) + ((0.4275 * (temp))(windSpeed ** 0.16)))
    return w


def main():
    wind = int(0)
    temp = int(-20)
    print("wind 0 - 50, temp -20 - 60")
    print("\t|\t-20\t|\t-10\t|\t0\t|\t10\t|\t20\t|\t30\t|\t40\t|\t50\t|\t60")
    for i in range (5):
        wind = wind + 5
        print("\n", wind, end ="\t|\t")
        for i in range(9):
            temp = temp + 10
            wc = windchill(int(wind), int(temp))
            print(round(wc ,1), end = "\t|\t")
        
main()




    
    
    

