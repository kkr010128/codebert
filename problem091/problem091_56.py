def resolve():
    # 最長の辺の長さ < 他の辺の長さの合計 で三角形
    N = int(input())
    lines = map(int, input().split())
    #N = 100
    #from random import randint
    #lines = [randint(1, 10 ** 9) for x in range(N)]
    from itertools import combinations
    count = 0
    for c in combinations(lines, 3):
        if len(set(c)) != 3:
            continue
        if max(c) < sum(c)-max(c):
            count += 1
    print(count)
resolve()