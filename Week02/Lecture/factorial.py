def factorial_recurive(n):
    if n == 1:
        return 1
    return n * factorial_recurive(n-1)

def factorial_nonrecursive(n):
    res = 1
    for i in range(n, 0, -1):
        res *= i
    return res

# main
if __name__ == "__main__":
    res = factorial_recurive(4)
    print(res)
    res2 = factorial_nonrecursive(4)
    print(res2)