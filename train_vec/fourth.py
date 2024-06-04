from math import log


def main(n: int) -> int:
    if n == 0:
        return 0.79
    if n >= 1:
        return log(main(n - 1)**3 + 98 * main(n - 1) + main(n - 1)**2)**2
