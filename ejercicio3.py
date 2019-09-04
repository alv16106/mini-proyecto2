import random
import numpy as np
import matplotlib.pyplot as plt
from get_distributions3 import get_first_dist, get_second_dist


def vpn(fluxes, k, Io):
    return -Io + sum(flux / (1 + k)**(i + 1) for i, flux in enumerate(fluxes))


def exponential(l):
    return np.log(1 - random.random()) / -l


def normal_dist_random(mu, sigma):
    while True:
        y1 = exponential(1)
        y2 = exponential(1)
        if y2 - ((y1 - 1)**2) / 2 > 0:
            y1 = y2 - ((y1 - 1)**2) / 2
            rand = random.random()
            if rand < 0.5:
                return mu + sigma*y1
            else:
                return mu - sigma*y1


def get_fluxes(distributions):
    fluxes = []
    for item in distributions:
        if item['type'] == 'normal':
            fluxes.append(normal_dist_random(*item['limits']))
            continue
        fluxes.append(random.randint(*item['limits']))
    return fluxes


def simulate(distributions, k,  n=10000):
    # recieves list of objects like {'type': 'normal', 'limits': (a,b)}
    s = distributions[0]['start']
    results = [vpn(get_fluxes(distributions[1:]), k, s) for i in range(n)]
    return sum(results) / n


if __name__ == "__main__":
    # Get the 2 distributions
    d1 = get_first_dist()
    d2 = get_second_dist()

    # SImulate for 100, 1000 and 10000
    repetitions = [100, 1000, 10000]
    fp = [simulate(d1, 0.1, r) for r in repetitions]
    sp = [simulate(d2, 0.1, r) for r in repetitions]
    print(fp)
    print(sp)

    # Graphs
    n_groups = 3

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(
        index,
        fp,
        bar_width,
        alpha=opacity,
        color='c',
        label='First Project')

    rects2 = plt.bar(
        index + bar_width,
        sp,
        bar_width,
        alpha=opacity,
        color='tomato',
        label='Second Project')

    plt.ylabel('VPN')
    plt.title('VPN for two projects')
    plt.xticks(index + bar_width, ('10', '1000', '10000'))
    plt.legend()

    plt.tight_layout()
    plt.show()
