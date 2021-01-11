#   fule.py
#   A program that finds the fule effeiceny
#   File: L08-10
#   by: Matthew Wilde   
#   11-16-2020
#   Practice file ext: C:\Users\Mattw\Desktop\L8_10File.txt


def gasC(miles, gas):
    total = (miles / gas)
    
    return total




def main():
    overAll = []
    finalMPG = 0
    x = 0
    
    
    fileExt = input("What is the file extention for a file you want to analyize ")
    content = open(fileExt, "r")
    legs = content.readline()
    allLines = content.readlines()
    
    for i in range(int(legs)):
        input_string = allLines[x]
        x = x + 1
        
        
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

