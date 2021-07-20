# Project Euler 2 - Even Fibonacci Numbers
# GitHub: urtuba

def evenFibonacciGenerator(limit: int):
    '''
    The function to create a generator for even fibonacci numbers

    :param limit: maximum number for the generator
    :return: even fibonacci numbers generator
    '''
    fib = 1
    fib_next = 2
    while (fib_next < limit):
        fib, fib_next = fib_next, fib_next + fib
        if fib % 2 == 0:
            yield fib

if __name__ == '__main__':
    even_fib_generator_4m = evenFibonacciGenerator(4_000_000)
    result = sum(even_fib_generator_4m)
    print(result)