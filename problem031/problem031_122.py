while True:
    n = int(input())
    if n == 0: break
    s = list(map(float, input().split()))
    m = sum(s) / n
    a = (sum((s[i] - m) ** 2 for i in range(n)) / n) ** 0.5
    print(a)