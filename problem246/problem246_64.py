n = int(input())
p = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]

pos = [None, None]


def fn(digits, maxlen, index, pos):
    for x in range(1, maxlen + 1):
        if x in digits:
            continue
        ndigits = digits + [x]
        if len(ndigits) < maxlen:
            index = fn(digits + [x], maxlen, index, pos)
        else:
            if ndigits == p:
                pos[0] = index
            if ndigits == q:
                pos[1] = index
            index = index + 1
            # print(f"{index}:" + " ".join(str(x) for x in ndigits))
    return index


fn([], n, 0, pos)
print(abs(pos[0] - pos[1]))
