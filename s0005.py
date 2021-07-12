# Euler 5 - Smallest Multiple
# Github: urtuba

from functools import reduce
from collections import defaultdict

def find_factors(num:int) -> defaultdict:
    '''
    Finds factors of a number and their recurrence to create the number.

    :param num: the number
    :return: default dict, keys represent factors, values are recurrence
    '''
    factors = dict()
    factors = defaultdict(lambda: 0, factors)
    start = 2
    while True:
        if num % start == 0:
            factors[start] += 1
            num = num / start
        else:
            start += 1

        if start > num:
            break
    return factors

def smallest_evenly_divisible(num:int) -> int:
    '''
    Takes a number and finds the smallest number which is evenly divisible
    to all numbers upto given number.

    :param num: the number
    :return: smallest evenly divisible number
    '''
    all_factors = defaultdict(lambda: 0, dict())
    for num in range(2, num):
        num_factors = find_factors(num)
        for key, val in num_factors.items():
            if all_factors[key] < val:
                all_factors[key] = val

    factors_list = []
    for key, val in all_factors.items():
        for i in range(val):
            factors_list.append(key)
    
    return reduce(lambda x, y: x*y, factors_list)

if __name__ == '__main__':
    result = smallest_evenly_divisible(20)
    print(result)
