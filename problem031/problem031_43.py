import sys, math
while True:
    n = int(input())
    if n == 0:
        sys.exit()
    s = list(map(int, input().split()))
    m = sum(s) / n
    S = 0
    for i in range(n):
        S += (s[i] - m) ** 2
    S /= n
    a = math.sqrt(S)
    print(a)
