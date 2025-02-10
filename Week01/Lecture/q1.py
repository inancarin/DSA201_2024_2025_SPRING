def findTheMostFreq(myList):
    d = {}

    for elem in myList:
        if elem not in d:
            #add this elem to dict with freq 1
            d[elem] = 1
        else:
            d[elem] += 1
    
    keys = []
    maxValue = max(d.values())
    for k, v in d.items():
        if v == maxValue:
            keys.append(k)
    return min(keys)


# main part
arr = [1,1, 2, 2, 3]
print(findTheMostFreq(arr))
