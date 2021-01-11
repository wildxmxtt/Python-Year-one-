#   easter.py
#   File name: L07-10
#   Description: A program that
#   By: Matthew Wilde
#   11-9-2020

def easter(year):
    a = year%19
    b = year%4
    c = year%7
    d = ((19 * a) + 24)%30
    e = ((2 * b)+(4 * c)+(6 * d) + 5)%7

    ans = d + e
    
    return ans

    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        return ans - 7

    
    
    


def main():
    year = int(input("What is the year betweeen 1982 and 2048: "))
    if year < 1900 or year > 2099:
               print("Out of range please select a year betweeen 1982 and 2048")
               year = int(input("What is the year: "))

    e = easter(year)

    print("The date of easter is:",e)
    
main()
