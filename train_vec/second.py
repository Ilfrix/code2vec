from math import tan, floor


def main(z):
    if z < 86:
        return 0.03 - z**5
    elif 86 <= z and z < 123:
        return 36 * z**4 - (floor(32 * z**2 - 94 * z**3 - 46 * z))**7 - 40
    elif 123 <= z and z < 212:
        return 41 * (floor(z)**5) - tan(z**2 / 56 - 0.08 - z**3)
    elif 212 <= z and z < 236:
        return (84 * z**2 + 26 * z**3)**5 + 34 * z**4
    else:
        return 40 * z**6 + 71 * z**7
