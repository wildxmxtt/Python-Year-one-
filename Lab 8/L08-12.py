#   heatingandcooling.py
#   A program that caluates daily cooling a heating days
#   File: L08-11
#   by: Matthew Wilde   
#   11-16-2020
#   C:\Users\Mattw\Desktop\L8_12File.txt

def avgTemp(allTemps):
    x = 0
    hot = 0
    cold = 0
    temps = []
    
    for i in range(len(allTemps)):
        if int(allTemps[x]) < 60:
            hot = hot + 1
        if int(allTemps[x]) > 80:
            cold = cold + 1
        else:
            cold = cold + 0
            hot = hot + 0

        x = x + 1

    temps.append(cold)
    temps.append(hot)
        
    return temps
    


def main():
    allTemps = []
    x = 0 
    
    fileExt = input("What is the file extention for a file you want to analyize ")
    content = open(fileExt, "r")
    days = content.readline()
    allLines = content.readlines()
    for i in range(int(days)):
        temp = allLines[x]
        x = x + 1

        allTemps.append(temp)
        t = avgTemp(allTemps)
        

    print("The days spent cooling would be", t[0], "The days heating would", t[1])

main()
