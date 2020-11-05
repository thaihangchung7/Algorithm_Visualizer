def insertionsort(testarray):
    for i in range(1,len(testarray)):
        if testarray[i-1] > testarray[i]:
            testarray.insert(0,testarray[i])
        
        elif testarray[i-1] <= testarray[i]:
            pass
