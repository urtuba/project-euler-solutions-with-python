# Project Euler 4 - Largest Palindrome Product
# GitHub: urtuba

def is_palindrome(num: int) -> bool:
    '''
    Checks if given number is a palindrome.

    :param num: given number
    :return: result of check
    '''
    number = str(num)
    length = len(number)
    for i in range(int(length/2)):
        if number[i] != number[length-1-i]:
            return False
    return True

def largest_palindrome_product(digits: int) -> int:
    '''
    Finds largest palindrome product of numbers with n digits.

    :param digits: number of digits
    :return: largest palindrome product
    '''
    maximum = 10**digits
    numbers = set()
    for x in range(maximum):
        for y in range(maximum):
            numbers.add(x*y)
    numbers = list(numbers)
    numbers.sort(reverse=True)

    for num in numbers:
        if is_palindrome(num):
            return num

if __name__ == '__main__':
    result = largest_palindrome_product(3)
    print(result)