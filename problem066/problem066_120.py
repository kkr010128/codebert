XS = open(0).read().split()
i = 0
while True:
    t = XS[i]
    i += 1
    if t == "-":
        break
    n = int(XS[i])
    i += 1
    m = sum(map(int, XS[i:i+n])) % len(t)
    i += n
    print(t[m:] + t[:m])
