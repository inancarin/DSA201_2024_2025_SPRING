def someFunc(a, b):
    print("Some process will be executed here!")
    for i in range(5):
        a += 10
    b += 100
    print("End of the function")


# main part
x = 10
y = 20
someFunc(x, y)
print("End of the program")
