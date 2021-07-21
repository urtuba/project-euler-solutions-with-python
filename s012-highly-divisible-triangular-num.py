# Project Euler 12: Highly divisible triangular number
# GitHub: urtuba

from collections import defaultdict
from functools import reduce
from sys import maxsize

def number_of_divisors(number: int) -> int:
    '''
    Finds number of divisors/factors of a given number.

    :param number: number to find its divisors
    :return: count of divisors
    '''
    divisors = defaultdict(lambda: 0)
    divisor = 2
    while number != 1:
        if number % divisor == 0:
            number = number / divisor
            divisors[divisor] += 1
        else:
            divisor += 1
    return reduce(lambda x,y: x * (y+1), divisors.values(), 1)
    
def triangular_number_generator() -> int:
    '''
    Triangular number generator.

    :return: next triangular number until sys.maxsize
    '''
    triangular_number = 1
    for counter in range(2, maxsize):
        yield triangular_number
        triangular_number += counter

def highly_divisible_triangular_n(over: int) -> int:
    '''
    Finds minimum triangular number that has divisiors over 'over'.

    :param over: used in comparison, factor count should be larger than 'over'
    :return: minimum number which satisfies function's condition.
    '''
    trig_gen = triangular_number_generator()
    number = 0
    while True:
        number = next(trig_gen)
        if number_of_divisors(number) > over:
            return number

if __name__ == '__main__':
    result = highly_divisible_triangular_n(500)
    print(result)