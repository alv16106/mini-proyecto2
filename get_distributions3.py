def get_first_dist():
    dist = [
        {'start': 800},
        {'type': 'normal', 'limits': (-800, 50)},
        {'type': 'normal', 'limits': (-800, 100)},
        {'type': 'normal', 'limits': (-700, 150)},
        {'type': 'normal', 'limits': (300, 200)},
        {'type': 'normal', 'limits': (400, 200)},
        {'type': 'normal', 'limits': (500, 200)},
        {'type': 'uniform', 'limits': (200, 8440)},
    ]
    return dist


def get_second_dist():
    dist = [
        {'start': 900},
        {'type': 'normal', 'limits': (-600, 50)},
        {'type': 'normal', 'limits': (-200, 50)},
        {'type': 'normal', 'limits': (-600, 100)},
        {'type': 'normal', 'limits': (250, 150)},
        {'type': 'normal', 'limits': (350, 150)},
        {'type': 'normal', 'limits': (400, 150)},
        {'type': 'uniform', 'limits': (1600, 6000)},
    ]
    return dist
