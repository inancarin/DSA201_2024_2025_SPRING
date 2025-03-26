import clock

c = clock.Clock(23, 59, 54)
print(c)

for i in range(10):
    c.tick()
    print(c)