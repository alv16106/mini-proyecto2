import random
import numpy as np
import matplotlib.pyplot as plt

ITERATIONS = 10000


def plot_bar_x(values, frequency, title='Title'):
    objects = tuple(values)
    y_pos = np.arange(len(objects))

    plt.bar(y_pos, frequency, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Porcentajes')
    plt.title(title)
    plt.savefig('demo.png', bbox_inches='tight')


def random_weighted(fi, p):
    """ if p.sum() != 1:
        raise Exception('The sum of the p (probabilities) should be 1 not ' +
                        str(p.sum()))
        return """

    if v.shape != p.shape:
        raise Exception('v and p shape shoul be the same')
        return

    def f():
        ac = 0
        for i in range(0, len(fi)):
            r = random.random()
            ac = ac + p[i] * fi[i](r)

        return ac

    return f


f = random_weighted([], [])
a = np.zeros(ITERATIONS)

for i in range(0, ITERATIONS):
    a[i] = f()
