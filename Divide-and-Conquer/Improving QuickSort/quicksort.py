# python3

from random import randint


def partition3(array, left, right):
    x, j, t = array[left], left, right
    i = j

    while i <= t:
        if array[i] < x:
            array[j], array[i] = array[i], array[j]
            j += 1
        elif array[i] > x:
            array[t], array[i] = array[i], array[t]
            t -= 1
            i -= 1
        i += 1
    return j, t


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    return [randomized_quick_sort(array, left, m1-1), randomized_quick_sort(array, m2 + 1, right)]


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
