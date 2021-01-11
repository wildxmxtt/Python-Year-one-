#   speedingTicket.py
#   File name: L07-06
#   Description: A program that calculates speeding tickets
#   By: Matthew Wilde
#   10-27-2020

def ticket(speed, limit):
    tPrice = 0
    amountOver = speed - limit
    if speed > limit:
        tPrice = (amountOver * 5) + 50
    if speed >= 90:
        tPrice = tPrice + 200

    elif speed < limit:
        print("Congrats you werent speeding!")
        
    return tPrice


def main():
     

    speed = int(input("How fast were you going (mph): "))
    limit = int(input("What was the speed limit: "))

    r = ticket(speed, limit)

    print("The ticket price is $", r)
    



main()
