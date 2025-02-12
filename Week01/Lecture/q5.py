import math

def encrypt(s):
    s = s.replace(" ", "")
    L = len(s)
    print(L)

    val = math.sqrt(L)
    row = int(val)
    col = row
    if row < val:
        col += 1

    mat = []
    for i in range(row):
        temp = []
        for j in range(col):
            if i * col + j < L:
                temp.append(s[i * col + j])
            else:
                temp.append("")
        mat.append(temp)

    """
    mat = [
        ["i", "f", "m", "a", "n", "w", "a", "s"],
        ["m", "e", "a", "n", "t", "t", "o", "s"],
        ...
        ["s", "r", "o", "o", "t", "s", "", ""]
    ]
    """

    res = ""
    for j in range(col):
        for i in range(row):
            res += mat[i][j]
        res += " "
    
    return res

# main

res = encrypt("have a nice day")
print(res)
