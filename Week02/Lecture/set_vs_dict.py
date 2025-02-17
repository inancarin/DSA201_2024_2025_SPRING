def findMostCommonChar(s):
    d = {}
    for ch in s.lower():
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    
    maxVal = max(d.values())
    for k, v in d.items():
        if v == maxVal:
            print(k, v)


def findUniqueCharNum(s):
    mySet = set(s.lower())
    """
    mySet = set()
    for ch in s.lower():
        mySet.add(ch)
    """
    
    print(len(mySet))

if __name__ == "__main__":
    findMostCommonChar("Ankara")
    findUniqueCharNum("Ankara")