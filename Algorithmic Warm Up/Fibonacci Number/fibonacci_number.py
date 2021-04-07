# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    if n <= 1:
        return n

    arr = [0, 1]
    for d in range(2, n+1):
        val = d if d <= 1 else arr[d-1] + arr[d-2]
        arr.insert(d, val)
    return arr[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
