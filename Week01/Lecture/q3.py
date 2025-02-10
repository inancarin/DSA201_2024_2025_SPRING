matrix = [
          [1, 2, 3, 100, 20],
          [4, 5, 6, 30, 1000],
          [9, 8, 10, 4, 25],
          [198, 10, 20, 30, 40],
          [77, 66, 55, 44, 33]
        ]

sum1, sum2 = 0, 0

for i in range(len(matrix)):
    val1 = matrix[i][i]
    sum1 += val1

    val2 = matrix[i][len(matrix)-1-i]
    sum2 += val2

diff = abs(sum1 - sum2)
print(diff)
