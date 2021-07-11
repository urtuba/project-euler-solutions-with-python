# Euler 2 - Even Fibonacci Numbers
# Github: urtuba

from typing import Generator


def evenFibonacciGenerator(limit: int):
    '''
    The function to create a generator for even fibonacci numbers

    :param limit: maximum number for the generator
    :return: even fibonacci numbers generator
    '''
    fibTemp1 = 1
    fibTemp2 = 2
    while (fibTemp2 < limit):
        fibTemp1, fibTemp2 = fibTemp2, fibTemp2 + fibTemp1
        if fibTemp1 % 2 == 0:
            yield fibTemp1


if __name__ == '__main__':
    evenFibGen4m = evenFibonacciGenerator(4000000)
    result = sum(evenFibGen4m)
    print(result)