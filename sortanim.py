from bubblesort import bubblesort
from mergesort import mergesort
from insertionsort import insertionsort


#int array from user input
try:
    testarray = []
    print("Type in a array, press any key other than a number to submit array")
    while True:
        testarray.append(int(input()))
except:
    print("You entered: ",testarray)

#sort method from user input
method = input("Choose a sorting method: \n(b)ubblesort \n(m)ergesort \n(i)nsertionsort \n")

if method == "b":
    print("Array bubblesorted: ", bubblesort(testarray))
elif method == "m":
    print("Array mergesorted: ", mergesort(testarray))
elif method == "i":
    print("Array insertsorted: ", insertionsort(testarray))

else:
    print("That wasn't an option!")



