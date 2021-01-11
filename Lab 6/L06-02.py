#   AntsGoMarching.py
#   File name: L06-02
#   Descrption: A program that prints the ants go marching
#   By: Matthew Wilde 10-28-2020




def main():

    num = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    ry =["tie his shoe", "spit his gum", "slip and jump", "lean and turn", "criss and cross", "yell and shout", "whine and complain", "stop to watch anime", "throw and shove", "reem and lunge"]
    x = 0
    
    
    for i in range (10):
        print("The ants go marching", num[x], "by", num[x], ", hurrah! hurrah!")
        print("The ants go marching", num[x], "by", num[x], ", hurrah! hurrah!")
        print("The ants go marching", num[x], "by", num[x])
        print("THe little one stops to", ry[x])
        print("In the ground ... \n", "To get out ....Of the rain. \n","Boom! Boom! Boom! \n")
        x = x + 1
main()
