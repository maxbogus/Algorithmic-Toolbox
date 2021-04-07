# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    def majority_element_rec(lo, hi):
        if lo == hi:
            return 1

        mid = (hi-lo)//2 + lo
        left = majority_element_rec(lo, mid)
        right = majority_element_rec(mid+1, hi)

        if left == right:
            return 1

        left_count = sum(1 for i in range(lo, hi+1) if elements[i] == left)
        right_count = sum(1 for i in range(lo, hi+1) if elements[i] == right)
        if left_count > len(elements)/2 or right_count > len(elements)/2:
            return 1
        return 0
    return majority_element_rec(0, len(elements)-1)



if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
