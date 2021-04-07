# python3

from sys import stdin


def maximum_gold(W, golds):
    # assert 1 <= capacity <= 10 ** 4
    # assert 1 <= len(weights) <= 10 ** 3
    # assert all(1 <= w <= 10 ** 5 for w in weights)

    # weights_size = len(weights)
    # gold_amount = weights_size + 1
    # knapsack = [[0 for x in range(0, capacity+1)] for x in range(0, gold_amount)]
    #
    # for i in range(0, weights_size+1):
    #     for j in range(0, capacity+1):
    #         val = weights[i-1]
    #         if i == 0 and j == 0:
    #             knapsack[i][j] = 0
    #         elif val <= j:
    #             knapsack[i][j] = max(val + knapsack[i-1][j-val], knapsack[i-1][j])
    #         else:
    #             knapsack[i][j] = knapsack[i-1][j]
    #
    # return knapsack[weights_size][capacity]
    # We can compose weight 0 by taking nothing
    d = [[True] + [False] * W]
    for i in range(len(golds)):
        # We copy previous row which corresponds to
        # solution of not taking current gold
        d.append(d[-1][:])
        for w in range(golds[i], W + 1):
            # Weight w can be composed either by not taking current
            # gold (d[-2][w]) or by taking it (d[-2][w - golds[i]])
            d[-1][w] = d[-2][w] or d[-2][w - golds[i]]
        # It is enough to keep only last row
        d = d[-1:]
    for w in range(W, -1, -1):
        # Return maximal weight w that has True in d
        if d[-1][w]:
            return w


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
