"""
Merge Sort: A 'divide and conquer' algorithm. Recursive divides input 
array and subsequent arrays into two halves, sorting the while array sizes
are 1. Then merges sorted arrays together.

Time Complexity O(nlogn)
"""
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
"""
try:
    testarray = []
    print("Type in a array, press any key other than a number to submit array")
    while True:
        testarray.append(int(input()))
except:
    print("You entered: ",testarray)
"""

def merge(array_a, array_b):
    array_c = []

    while len(array_a) > 0 and len(array_b) > 0:
        if(array_a[0] > array_b[0]):
            array_c.append(array_b[0])
            #array_b.pop(array_b[0])
            del array_b[0]
        else:
            array_c.append(array_a[0])
            #array_a.pop(array_a[0])
            del array_a[0]
        
    while(len(array_a) > 0):
        array_c.append(array_a[0])
        #array_a.pop(array_a[0])
        del array_a[0]
    while(len(array_b) > 0):
        array_c.append(array_b[0])
        #array_b.pop(array_b[0])
        del array_b[0]

    return array_c
        

def mergesort(array):
    if len(array) == 1:
        return array

    else:
        half = len(array)//2
        array_1, array_2 = array[:half],array[half:]

        array_1 = mergesort(array_1)
        array_2 = mergesort(array_2)

        return merge(array_1,array_2)


    



#print("Merge sorted array: ", mergesort(testarray))

