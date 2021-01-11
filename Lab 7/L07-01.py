#   paymentpgrm.py
#   File name: L07-01
#   Description: A program that  pay time-and-a-half for any hours worked above 40 in a given week.
#   By: Matthew Wilde
#   10-27-2020

def main():
    hourlyPay = int(input("what is your hourly pay "))
    uHours = int(input("How many hours did you work in a week: ")) 
    
    rPay = 0
    tHP = 0
    finalPay = 0
    hOver = uHours - 40


    rPay = uHours * hourlyPay

    if uHours > 40:
        for i in range(hOver):
            tHP = (hourlyPay * 1.5) * hOver

    finalPay = rPay + tHP

    print("you paycheck will be $", finalPay)
    
main()


