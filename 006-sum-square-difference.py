# Project Euler 6 - Sum Square Difference
# GitHub: urtuba

def squares_difference(upto:int) -> int:
    '''
    Function which calculates the difference between the square of sums and
    the sum of squares.
    
    :param upto: last number of series 1, 2, ..., upto
    :return: (1+2+..+upto)^2 - (1^2+2^2+..+upto^2)
    '''
    nums = list(range(1, upto+1))
    return sum([x*y for x in nums for y in nums if x!=y])

if __name__ == '__main__':
    result = squares_difference(20)
    print(result)