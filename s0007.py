# Euler 7 - Nth Prime Number
# Github: urtuba

import numpy as np
MAX = 200000

def is_prime(num: int) -> bool:
    '''
    Checks that given number is prime number.

    :param num: number to check
    :return: boolean
    '''
    max = int(num**0.5) + 1
    for i in range(2, max):
        if num % i == 0:
            return False
    return True

def create_primes_array(maximum:int) -> np.array:
    '''
    Function to get array of prime numbers.

    :param maximum: maximum value
    :return: np array of prime numbers
    '''
    numbers = np.array(np.arange(2, maximum))
    primes = np.array([])
    
    for num in numbers:
        if is_prime(num):
            primes = np.append(primes, np.array([num]))
            numbers = numbers[numbers % num != 0]

    return primes

def nth_prime_number(n:int) -> int:
    '''
    Function to get Nth prime number.

    :param n: order of the prime number
    :return: Nth prime number
    '''
    primes = create_primes_array(MAX)
    return int(primes[n-1])

if __name__ == '__main__':
    result = nth_prime_number(10001)
    print(result)