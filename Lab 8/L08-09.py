#   fule.py
#   A program that finds the fule effeiceny
#   File: L08-09
#   by: Matthew Wilde   
#   11-16-2020


def gasC(miles, gas):
    total = (miles / gas)
    
    return total




def main():
    overAll = []
    finalMPG = 0
    x = 0
    
    legs = int(input("How many legs of the trip are there: "))
    
    for i in range(legs):
        x = i + 1
        print("What dose your odometer read and the amount of gas used for leg", x)
        input_string = input("Enter here: ")
        
        userList = input_string.split()
        odometer = int(userList[0])
        gasUsed = int(userList[1])
        
        g = gasC(odometer, gasUsed)
        totalMPG = overAll.append(g)
            
        print("The gas used on leg", i + 1, "was", g, "\n")
    
    for i in range(len(overAll)):
        finalMPG = finalMPG + overAll[i]
        
    print("The over all MPG was", finalMPG)
    
main()
