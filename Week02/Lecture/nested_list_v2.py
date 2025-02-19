def findFreq(names, counts):
    for name in names:
        if not isinstance(name, list):
            if name in counts:
                counts[name] += 1
            else:
                counts[name] = 1
        else:
            findFreq(name, counts)

if __name__ == "__main__":
    names = ["Adam", ["Bob", ["Alex","Bob"], "Barb", "Bert"], "Alex", ["Bea", "Alex"], "Ann"]
    counts = {} # dict()
    findFreq(names, counts)
    print(counts)