import re
import string

    #python function to split the passed string into a list
def splitFoodString(foodString):
    
    foodList = foodString.split()
    
    return foodList
#python function to search the food list for a item and display its frequency
def searchCount(foodString):
    #declaring local variables
    count = 0
    counter = 0
    countz=0
    test = False
    outList = []
    newList = []
    freqList = []
    foodList = splitFoodString(foodString)
    #logic loop to add all unique values to new loop
    for item in foodList:
        for new in newList:
            if item == new:
                test = True
        if test == False:
            newList.append(item)
        test = False

        #logic loop to add frequency behind the item value in the freq list
    for item in newList:
        for new in foodList:
            if item == new:
                counter = counter + 1

        freqList.append(str(item) + "\n")
        freqList.append(str(counter) + "\n")
        counter = 0

        #open file and write to frequency.dat
    file1 = open('frequency.dat', 'w')

    file1.writelines(freqList)

    file1.close()
    #ask user for input
    inp = input('Enter item to search for: ')

    file1 = open('frequency.dat', 'r')

    Lines = file1.readlines()
    #loop through list for input and if found then output the item and its frequency
    for line in Lines:

        if count == 1:
            count = 0
            print(line.strip("\n"))

        if line.strip("\n") == inp:
            print(line.strip("\n") + " ", end = "")
            count = 1

            #close file
    file1.close()

  
    return 100

def histo(foodString):
    #declare local variables
    counter = 0
    countz=0
    test = False
    outList = []
    newList = []
    freqList = []
    foodList = splitFoodString(foodString)
    #logic loop to create unique list of items called foodlist
    for item in foodList:
        for new in newList:
            if item == new:
                test = True
        if test == False:
            newList.append(item)
        test = False

        #logic loop to add frequency and unique items to freqlist
    for item in newList:
        for new in foodList:
            if item == new:
                counter = counter + 1

        freqList.append(str(item) + "\n")
        freqList.append(str(counter) + "\n")
        counter = 0

        #write freqlist to frequency.dat
    file1 = open('frequency.dat', 'w')

    file1.writelines(freqList)

    file1.close()
    #open frequency.dat to read
    file1 = open('frequency.dat', 'r')

    Lines = file1.readlines()
    #loops to print out histogram with unique items and frequency in "*"
    for line in Lines:

        if countz % 2 == 0:

           print(line.strip("\n"), end = "")

        else:
            holder = line.strip("\n")
            intholder = int(holder)
            for item in range(intholder):
                print("*",end = "")        
            print("")
        
        countz = countz + 1

    file1.close()

  
    return 100

def individualCount(foodString):
    #declare local variables
    counter = 0
    test = False
    newList = []
    #send parsed string from c++ to python splitfoodstringfunction to make it into a list
    foodList = splitFoodString(foodString)
    #loop to append unique items to new list
    for item in foodList:
        for new in newList:
            if item == new:
                test = True
        if test == False:
            newList.append(item)
        test = False


        #loop to print items and their frequencies
    for item in newList:
        for new in foodList:
            if item == new:
                counter = counter + 1
        print(str(item) + " " + str(counter))
        counter = 0

    return 100