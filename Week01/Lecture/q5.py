import math

s = "if man was meant to stay on the ground god would have given us roots"
s = s.replace(" ", "")
L = len(s)
print(L)

val = math.sqrt(L)
row = int(val)
col = row
if row < val:
    col += 1

print(row, col)
print(s)
"""
mat = [
    ["i", "f", "m", "a", "n", "w", "a", "s"],
    ["m", "e", "a", "n", "t", "t", "o", "s"],
    ...
    ["s", "r", "o", "o", "t", "s", "", ""]
]
"""