#   fibNum.py
#   File name: L06-07
#   Descrption: A program that finds the "nth" number of the fibonachii sequesnce
#   By: Matthew Wilde 10-28-2020

def fibS(rt): 
    j = 1
    k = 0
    fib = 0
    for i in range (rt):
        fib = j + k
        j = k
        k = fib

    print("The nth number is:", fib)

def main():
    runTime = int(input("How many numbers are to be summed "))

    fibS(runTime)

    
main()
