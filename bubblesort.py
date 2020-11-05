"""
Bubblesorting: swaping adjacent elements
that are in the wrong order. We keep interating
through swaps until there are no swaps left.
"""
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#defining swap function
def swap(A, i, j):
    if i != j:
        A[i], A[j] = A[j], A[i]


#actually bubblesorting
def bubblesort(A):

    if len(A)==1:
        return

    swapped = True
    for i in range(len(A)-1):

        if not swapped:
            break
        swapped = False
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
                swapped = True
    return A

