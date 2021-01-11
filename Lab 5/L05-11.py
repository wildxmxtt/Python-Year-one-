#File: chaos.py
#A program that prints a random numbers when in the range of 0 and 1
#Matthew Wilde
#09-3-2020

def main():
        print ("This program illustrates a chaotic function")
        y = eval(input("Enter a number between 0 and 1: "))
        x = eval(input("Enter another number between 0 and 1: "))
        print("index    ", "{0: <12} ".format(y), "{0: <12} ".format(x))
        print("-----------------------------------")
        for i in range (10):
            y = 3.9 * y * (1 - y)
            x = 3.9 * x * (1 - x)
            print(i + 1, "     ", "{0: <12} ".format(round(y, 6)), "{0: <12} ".format(round(x, 6)))

            
main()
