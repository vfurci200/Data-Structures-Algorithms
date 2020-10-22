# python3
import time

def max_pairwise_product(numbers):

    index = numbers.index(max(numbers))
    max1 = numbers.pop(index)
    max_product = max1 * max(numbers)

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
