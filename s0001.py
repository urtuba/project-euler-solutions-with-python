# Euler 1 - Multiples of 3 and 5
# Github: urtuba

def multiples_of(x, y, r):
    '''
    multiplesOf function creates a generator which generates numbers divisible
    by two numbers.
    
    :param x: first number
    :param y: second number
    :param r: range, maximum possible number + 1
    :return: x-y-divisible number generator
    '''
    for i in range(r):
        if (i % x == 0) or (i % y == 0):
            yield i

if __name__ == '__main__':
    multiples_of_3_and_5 = multiples_of(3, 5, 1000)
    result = sum(multiples_of_3_and_5)
    print(result)

