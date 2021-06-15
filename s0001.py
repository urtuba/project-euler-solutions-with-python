#1 Multiples of 3 and 5
def multiplesOf(x, y, r):
    for i in range(r):
        if (i % x == 0) or (i % y == 0):
            yield i
multiplesOf3and5 = multiplesOf(3, 5, 1000)

print(sum(multiplesOf3and5))

