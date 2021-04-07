# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def gcd(a, b):
    if b == 0:
        return a
    remainder = a % b
    return gcd(b, remainder)


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    first_index = None
    for i in range(len(numbers)):
        if first_index is None:
            first_index = i
        else:
            if numbers[i] >= numbers[first_index]:
                first_index = i

    second_index = None
    for i in range(len(numbers)):
        if i != first_index:
            if second_index is None:
                second_index = i
            else:
                if numbers[i] >= numbers[second_index]:
                    second_index = i

    return numbers[first_index] * numbers[second_index]


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
