def someFunc(a, b):
    print("Some process will be executed here!")
    for i in range(5):
        a += 10
    b += 100
    print("End of the function")

def anotherFunc(s):
    if len(s) > 5:
        check = True
    if check:
        print("The length of the string is greater than 5")
    else:
        print("The length of the string is not greater than 5")


# main part
x = 10
y = 20
someFunc(x, y)
anotherFunc("dsa201")
print("End of the program")
