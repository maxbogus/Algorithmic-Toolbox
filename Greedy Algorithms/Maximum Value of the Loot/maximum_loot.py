# python3

from sys import stdin
import collections


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    inv = {}

    for i in range(len(weights)):
        inv[prices[i] / weights[i]] = i

    od = collections.OrderedDict(sorted(inv.items(), reverse=True))

    result = 0
    for k in od:
        if capacity == 0:
            return result
        limit = min(capacity, weights[od[k]])
        capacity -= limit
        result += (prices[od[k]] / weights[od[k]]) * limit

    return result


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
