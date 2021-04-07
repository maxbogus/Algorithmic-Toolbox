# python3


def edit_distance(first_string, second_string):
    m = len(first_string) + 1
    n = len(second_string) + 1
    tbl = {}
    for i in range(m): tbl[i, 0]=i
    for j in range(n): tbl[0, j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if first_string[i-1] == second_string[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)
    return tbl[i, j]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
