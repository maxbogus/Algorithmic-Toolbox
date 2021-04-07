# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    result = 0
    if money >= 10:
        result += money // 10
        money -= (money // 10) * 10
    if money >= 5:
        result += money // 5
        money -= (money // 5) * 5
    result += money
    return result


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
