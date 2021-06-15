#2 Even Fibonacci Numbers

def evenFibonacciGenerator(limit):
    fibTemp1 = 1
    fibTemp2 = 2
    while (fibTemp2 < limit):
        fibTemp1, fibTemp2 = fibTemp2, fibTemp2 + fibTemp1
        if fibTemp1 % 2 == 0:
            yield fibTemp1

evenFibGen4m = evenFibonacciGenerator(4000000)
print(sum(evenFibGen4m))