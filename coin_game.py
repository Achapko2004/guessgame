from random import choice
from collections import Counter, namedtuple
from pprint import pformat, pprint

def simulate():
    prev = -1
    while True:
        curr = choice((0, 1))
        yield curr
        if prev == curr == 0:
            break
        prev = curr

def simulate_game(n):
    s = 0
    c = Counter()
    for i in range(n):
        res = sum(simulate())
        s += res
        c.update([res])
    return {"n_sims": n, "avg_win": s / n, "distribution": dict(c)}

