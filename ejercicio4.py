import random


def probability_maker(params):
    def prob():
        rand = random.random()
        if rand < params[0]:
            return 9
        if rand < params[1]:
            return 10
        return 11
    return prob


def earnings(cost, sale, daily, price, r):
    if sale < daily:
        return sale * (price - cost) + (sale - daily) * (cost - r)
    return daily * (price - cost)


def simulate(cost, price, buyback, daily, n=30):
    r_sales = probability_maker((0.3, 0.7, 1))
    sales = [r_sales() for i in range(n)]
    return sum(earnings(cost, sale, daily, price, buyback) for sale in sales)


if __name__ == "__main__":
    r_sales = probability_maker((0.3, 0.7, 1))
    print(simulate(1.5, 2.5, 0.5, 9, 10))
    print(simulate(1.5, 2.5, 0.5, 10, 10))
    print(simulate(1.5, 2.5, 0.5, 11, 10))
