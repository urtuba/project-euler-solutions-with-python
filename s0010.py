# Project Euler 10 - Summation of primes
# GitHub: urtuba

def is_prime(num:int) -> bool:
    '''
    Checks that given number is prime number.

    :param num: number to check
    :return: boolean, is the num prime?
    '''
    if num < 2:
        return False

    max = int(num**0.5) + 1
    for i in range(2, max):
        if num % i == 0:
            return False
    return True

def prime_generator(max:int):
    for n in range(2,max):
        if is_prime(n):
            yield n

def summation_of_primes(max:int) -> int:
    '''
    Sums all prime number below 'max'.

    :param max: numbers will be checked if they are below max
    :return: sum of all primes below max
    '''
    return sum(prime_generator(max))

if __name__ == '__main__':
    result = summation_of_primes(2000000)
    print(result)
