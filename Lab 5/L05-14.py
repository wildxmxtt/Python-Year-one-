#   wcP5.py
#   File name: L05-014
#   A This program analyzes a file to determine the number of lines, words, and characters contained therein. 
#   by: Matthew Wilde
#   10-13-2020
#   Practice file ext: C:\Users\Mattw\Desktop\Lab14File.txt

def wordCount(content_sentence):
    split = len(content_sentence.split()) 
    
    print ("The number of words in string are : " +  str(split)) 


def chrCount(content_chrC):
    print ("The amount of characters in the document was: ",len(content_chrC))
    

def lineCount(content_lineC):
    counter = 0 
    lnCheck = content_lineC.split("\n")

    for i in lnCheck:
        if i:
            counter += 1
            
    print("The amount of lines in the document was: ", counter)
        
def main():
    fileExt = input("What is the file extention for a file you want to analyize ")
    content = open(fileExt, "r")
    content = (content.read())

    wordCount(str(content))
    chrCount(str(content))
    lineCount(str(content))

main()
