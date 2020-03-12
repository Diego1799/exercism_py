def encode(values):
    ret = []
    for value in values:
        a = []
        while True:
            a.append(value % 2**7)
            value = value // 2**7
            if value == 0:
                break
        for i in range(1, len(a)):
            a[i] += 128
        ret.extend(reversed(a))
    return ret


def decode(values):
    ret = []
    cur = 0
    b = 0
    for value in values:
        if not (0 <= value < 2**8):
            raise ValueError('Value range error')
        b = value // 2**7
        x = value % 2**7
        cur = cur * 2**7 + x
        if b == 0:
            ret.append(cur)
            cur = 0
    if b == 1:
        raise ValueError('Non found last zero block')
    return ret