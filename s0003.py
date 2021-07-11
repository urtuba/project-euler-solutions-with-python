# Euler 3 - Largest Prime Factor
# Github: urtuba

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

def largest_prime_factor(num: int) -> int:
    '''
    Finds largest prime factor of given number.

    :param num: given number
    :return: largest prime factor of num
    '''
    if is_prime(num):
        return num
    max = int(num**0.5) + 1
    for i in range(max, 1, -1):
        if num % i == 0:
            if is_prime(i):
                return i
    return 1

result = largest_prime_factor(600851475143)
print(result) 