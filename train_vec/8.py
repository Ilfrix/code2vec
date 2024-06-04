def main(val: tuple) -> str:
    res = 0
    for i in range(4):
        cur = int(val[i], 16)
        if i == 0:
            res += cur
        elif i == 1:
            res += cur << 1
        elif i == 2:
            res += cur << 11
        else:
            res += cur << 18
    return str(res)
