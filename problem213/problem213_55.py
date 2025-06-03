def abc156c_rally():
    n = int(input())
    x = list(map(int, input().split()))
    min_x, max_x = min(x), max(x)
    best = float('inf')
    for i in range(min_x, max_x + 1):
        total = 0
        for v in x:
            total += (v - i) * (v - i)
        if best > total:
            best = total
    print(best)

abc156c_rally()