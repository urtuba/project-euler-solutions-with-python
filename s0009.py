# Special Pythagorean Triplet
# Github: urtuba

def special_pythagorean_triplet(total:int) -> tuple:
    '''
    Finds the pythogorean triplet from sum of side lenghts if exists.

    :param total: Sum of side lenghts. E.g. 12 for 3-4-5 triangle.
    :return: tuple of  side lenghts of triangle. (a, b, c)
    '''
    for b in range(total):
        for a in range(b):
            if (a**2 + b**2) == (total - a - b)**2:
                return (a, b, total-a-b)

if __name__ == '__main__':
    triplet = special_pythagorean_triplet(1000)
    print('TRIANGLE:',triplet)
    product = triplet[0] * triplet[1] * triplet[2]
    print('PRODUCT: ', product)