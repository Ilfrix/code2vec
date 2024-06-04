from struct import *


FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d'
)


def parse(buf, offs, ty, order='<'):
    pattern = FMT[ty]
    size = calcsize(pattern)
    value = unpack_from(order + pattern, buf, offs)[0]
    return value, offs + size


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'int32')
    d2size, offs = parse(buf, offs, 'uint32')
    d2offs, offs = parse(buf, offs, 'uint32')
    d2 = []
    for _ in range(d2size):
        val, d2offs = parse(buf, d2offs, 'int16')
        d2.append(val)
    offs = d2offs
    return dict(D1=d1, D2=d2), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'double')
    c2, offs = parse(buf, offs, 'int8')
    return dict(C1=c1, C2=c2), offs


def parse_b(buf, offs):
    b1offs, offs = parse(buf, offs, 'uint16')
    b1, _ = parse_c(buf, b1offs)
    b2size, offs = parse(buf, offs, 'uint16')
    b2offs, offs = parse(buf, offs, 'uint32')
    b2 = ''
    for _ in range(b2size):
        val, b2offs = parse(buf, b2offs, 'char')
        b2 += val.decode('ascii')

    b3, offs = parse(buf, offs, 'uint8')
    b4 = []
    tmp_offs = offs
    for _ in range(7):
        address, tmp_offs = parse(buf, tmp_offs, 'uint32')
        val, _ = parse_d(buf, address)
        b4.append(val)
    b5 = []
    offs = tmp_offs
    for _ in range(3):
        val, offs = parse(buf, offs, 'uint16')
        b5.append(val)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5), offs


def parse_a(buf, offs):
    a1offs, offs = parse(buf, offs, 'uint16')
    a1, _ = parse_b(buf, a1offs)
    a2, offs = parse(buf, offs, 'int32')
    return dict(A1=a1, A2=a2), offs


def main(stream):
    res, _ = parse_a(stream, 4)
    return res
