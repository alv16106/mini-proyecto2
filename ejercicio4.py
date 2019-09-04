import random
import numpy as np
import matplotlib.pyplot as plt


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
    repetitions = [30, 365, 3650]
    nine = [simulate(1.5, 2.5, 0.5, 9, r) for r in repetitions]
    ten = [simulate(1.5, 2.5, 0.5, 10, r) for r in repetitions]
    eleven = [simulate(1.5, 2.5, 0.5, 11, r) for r in repetitions]

    bars = ('9', '10', '11')
    colors = ['chartreuse', 'c', 'tomato']
    y_pos = [0, 1, 2]

    for i in range(len(repetitions)):
        plt.figure(i)
        plt.bar(y_pos, [nine[i], ten[i], eleven[i]], color=colors)
        plt.xticks(y_pos, bars)

    plt.show()
