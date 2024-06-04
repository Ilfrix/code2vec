from math import ceil


def main(n: int, a: int, m: int, x: float) -> float:
    res = 0
    for j in range(1, m + 1):
        for k in range(1, a + 1):
            for c in range(1, n + 1):
                res += ceil(x) ** 7 - c**3 - 16 * (j**3 + k**2 + 1)**5
    return res
