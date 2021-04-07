# python3
def calc(a, b, op):
    """ Evaluates the expression (a op b)
    (int, int, char) -> (int) """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b


def min_and_max(M, m, i, j, operators):
    """ Finds the optimal values i.e. min and max for a subproblem
    (2D-array, 2D-array, int, int, list) -> (int, int) """
    min_value = float("inf")
    max_value = float("-inf")
    for k in range(i, j):
        a = calc(M[i][k], M[k+1][j], operators[k])
        b = calc(M[i][k], m[k+1][j], operators[k])
        c = calc(m[i][k], M[k+1][j], operators[k])
        d = calc(m[i][k], m[k+1][j], operators[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value


def get_maximum_value(operands, operators):
    n = len(operands)
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        m[i][i] = operands[i]
        M[i][i] = operands[i]

    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(M, m, i, j, operators)

    return M[0][n-1]


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    operators, operands = [], []

    for i in dataset:
        if i in ['+', '-', '*']:
            operators.append(i)
        else:
            operands.append(int(i))

    return get_maximum_value(operands, operators)


if __name__ == "__main__":
    print(find_maximum_value(input()))
