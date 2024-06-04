def main(y, z, x) -> float:
    res = 0.0
    for i in range(0, 3):
        res += 67 * (y[2 - i] ** 3 / 96 - 6 * x[i] - 2 * z[i]**2) ** 5

    return res
