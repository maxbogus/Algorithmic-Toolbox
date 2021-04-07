# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def sort_numbers(numbers):

    return numbers


def largest_number(numbers):
    numbers = sort_numbers(numbers)
    result = ''
    for number in numbers:
        result = '{}{}'.format(result, number)
    print(result, numbers)
    return int(result)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
