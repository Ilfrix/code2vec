from math import ceil


def calc_k(p: set) -> set:
    res = set()
    for val in p:
        if -34 < val < 47:
            res.add(val)
    return res


def calc_o(p: set) -> set:
    res = set()
    for val in p:
        if val <= -15:
            res.add(val)
    return res


def calc_teta(o: set) -> set:
    res = set()
    for val in o:
        if -59 <= val < 71:
            res.add(val + 9 * val)
    return res


def main(p: set) -> int:
    k = calc_k(p)
    teta = calc_teta(calc_o(p))
    tmp = k
    tmp.update(teta)
    res = len(tmp)
    for val in teta:
        res -= ceil(val / 8)
    return res
