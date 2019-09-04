import random
import numpy as np
from get_distributions3 import get_first_dist, get_second_dist


def vpn(fluxes=[], k=1, Io=1):
    return -Io + sum(flux / (1 + k)**(i + 1) for i, flux in enumerate(fluxes))


def exponential(l=5):
    return np.log(1 - random.random()) / -l


def normal_dist_random(mu=0, sigma=1):
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


def simulate(distributions, k, initial,  n=10000):
    # recieves list of objects like {'type': 'normal', 'limits': (a,b)}
    results = [vpn(get_fluxes(distributions), k, initial) for i in range(n)]
    return sum(results) / n


if __name__ == "__main__":
    d1 = get_first_dist()
    d2 = get_second_dist()
    print(simulate(d1, 0.1, 800))
    print(simulate(d2, 0.1, 900))
