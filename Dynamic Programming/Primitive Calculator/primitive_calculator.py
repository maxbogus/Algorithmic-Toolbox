# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    dp = [-1, 0]
    array = [0, 1]
    for i in range(2, n+1):
        count_3 = count_2 = count_1 = n
        if i % 3 == 0:
            count_3 = dp[int(i/3)]
        if i % 2 == 0:
            count_2 = dp[int(i/2)]
        if i - 1 >= 0:
            count_1 = dp[i-1]
        dp.append(min(count_3+1, count_2+1, count_1+1))
        if count_3 <= min(count_2, count_1):
            array.append(int(i/3))
        elif count_2 <= min(count_3, count_1):
            array.append(int(i/2))
        elif count_1 <= min(count_3, count_2):
            array.append(i-1)
    first = dp[n]
    array_2 = [n]
    print(first)
    for i in range(dp[n]):
        array_2.append(array[n])
        n = array[n]
    array_2.reverse()
    return array_2


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
