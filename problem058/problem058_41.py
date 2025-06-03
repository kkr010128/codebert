import sys

for line in sys.stdin:
    n,x = map(int,line.split())
    if n==0 and x==0:
        break
    _range = list(range(1,n+1))
    conb = []
    for i in _range[::-1]:
        d = x - i
        if i - 1 <= 0:
            continue
        for j in _range[:i-1][::-1]:
            d2 = d - j
            if j - 1 <= 0:
                continue
            for k in _range[:j-1][::-1]:
                if d2 - k == 0:
                    conb.append((i,j,k))

    print(len(conb))