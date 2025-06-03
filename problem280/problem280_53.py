def abc145c_average_length():
    import itertools
    import math
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    result = 0
    cnt = 0
    for p in itertools.permutations(range(n)):
        total = 0
        for i in range(n-1):
            total += math.sqrt(pow(x[p[i]]-x[p[i+1]], 2)+pow(y[p[i]]-y[p[i+1]], 2))
        result += total
        cnt += 1
    print(result/cnt)
abc145c_average_length()