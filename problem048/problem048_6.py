listed = []
nmin = 0
nmax = 0
nsum = 0

n = int(input())
if n > 0 and n <= 10000:
    listed = list(map(int, input().split(maxsplit=n-1)))
    nmin = listed[0]
    nmax = listed[0]
    for i in listed:
        if i >= -1000000 and i <= 1000000:
            if nmin > i:
                nmin = i
            if nmax < i:
                nmax = i
            nsum += i
        else:
            pass
else:
    pass

print("{0} {1} {2}".format(nmin, nmax, nsum))