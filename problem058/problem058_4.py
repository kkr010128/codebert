import itertools
while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break
    i = 0
    l = range(1, n+1)
    for elem in itertools.combinations(l, 3):
        if sum(elem) == x:
            i += 1
    print(str(i))