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


def random_weighted(v, p):
    """ if p.sum() != 1:
        raise Exception('The sum of the p (probabilities) should be 1 not ' +
                        str(p.sum()))
        return """

    if v.shape != p.shape:
        raise Exception('v and p shape shoul be the same')
        return

    def f():
        r = random.random()
        for i, value in enumerate(v):
            if r <= np.sum(p[0:i + 1]):
                return value

    return f


v = np.array([1, 2, 3, 4, 5, 6])
p = np.array([0.1, 0.1, 0.2, 0.3, 0.2, 0.1])
print(np.sum(p, dtype=np.double))
frequency = np.zeros(v.shape)

f = random_weighted(v, p)

for i in range(0, ITERATIONS):
    va = f()
    i, = np.where(v == va)
    frequency[i] = frequency[i] + 1

plot_bar_x(v, (frequency / ITERATIONS) * 100, title='Frecuencia')
