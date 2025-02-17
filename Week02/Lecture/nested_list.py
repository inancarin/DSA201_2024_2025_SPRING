def countLeafElements(myList):
    cnt = 0
    for elem in myList:
        if not isinstance(elem, list):
            cnt += 1
        else:
            cnt += countLeafElements(elem)
    return cnt

if __name__ == "__main__":
    names = ["Adam", ["Bob", ["Chet","Cat"], "Barb", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
    res = countLeafElements(names)
    print(res)