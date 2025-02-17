import time, factorial, math

if __name__ == "__main__":
    start = time.time()
    for i in range(1000000):
        res = factorial.factorial_recurive(100)
    end = time.time()
    elapsed = end-start
    print("Time elapsed recursive:", elapsed)

    start = time.time()
    for i in range(1000000):
        res = factorial.factorial_nonrecursive(100)
    end = time.time()
    elapsed = end-start
    print("Time elapsed nonrecursice:", elapsed)

    start = time.time()
    for i in range(1000000):
        res = math.factorial(100)
    end = time.time()
    elapsed = end-start
    print("Time elapsed math:", elapsed)