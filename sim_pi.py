import random
from collections import namedtuple, Counter
import math

Point = namedtuple("Point", "x, y")

center = Point(0.5, 0.5)

def distance(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def in_circle(p):
    return distance(p, center) <= 0.5

def random_points(N):
    from random import random

    for n in range(N):
        yield Point(random(), random())

def calc_pi(N=1000):
    n_in = 0
    for p in random_points(N):
        if in_circle(p):
            n_in += 1
    return n_in / N * 4




