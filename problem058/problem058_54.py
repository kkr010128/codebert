import itertools
while True:
    n,x = list(map(int, input().split()))
    if n == x == 0:
        break
    a = []
    for i in range(1, n+1):
        a.append(i)
    b = list(itertools.combinations(a,3))
    c = []
    for i in range(len(b)):
        if sum(b[i]) == x:
            c.append(b[i])
    print(len(c))