from math import sqrt


def main(z, y, x):
    return sqrt(52 * (y - 89 * x**2)**2 + 91 * abs(z)) - (19 * (z + x**3)**7 - 5 * y**3) \
        / ((92 * z**2 + 96 * x + y**3)**2 + 36 * y**6)


print("{:.2e}".format(main(8, 4, 4)))
