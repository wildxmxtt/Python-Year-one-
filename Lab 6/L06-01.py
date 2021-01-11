#   OldMacDonald.py
#   File name: L06-01
#   Description; A program that prints old Macdonald
#   By: Matthew Wilde
#   10-27-2020




def main():

    animal = ["cow", "sheep", "dog", "pig", "chicken"]
    animalNoise = ["moo", "baah", "wolf", "oink", "bak"]
    x = 0
    
    
    for i in range (5):
        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh! \n And on that farm he had a",animal[x], ", Ee-igh, Ee-igh, Oh! \n With a", animalNoise[x], animalNoise[x], "here and a" , animalNoise[x], animalNoise[x] ,", there")
        print("Here a", animalNoise[x], "there a", animalNoise[x], ", everywhere a", animalNoise[x], animalNoise[x], ".")
        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh! \n")
        x = x + 1
main()
