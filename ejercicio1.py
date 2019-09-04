import random
import numpy as np
import matplotlib.pyplot as plt
from ejercicio3 import normal_dist_random, exponential

ITERATIONS = 10000


def plot_bar_x(list, title='Title'):

    plt.hist(x=list, bins=50)
    plt.savefig('demo.png', bbox_inches='tight')


def random_weighted(fi, p):
    """ if p.sum() != 1:
        raise Exception('The sum of the p (probabilities) should be 1 not ' +
                        str(p.sum()))
        return """

    if len(fi) != len(p):
        raise Exception('v and p shape shoul be the same')
        return

    def f():
        ac = 0
        for i in range(0, len(fi)):
            ac = ac + p[i] * fi[i]()

        return ac

    return f


f = random_weighted([normal_dist_random, exponential], [0.1, 0.9])
a = np.zeros(ITERATIONS)

for i in range(0, ITERATIONS):
    a[i] = f()

plot_bar_x(a/ITERATIONS)
