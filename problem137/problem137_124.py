from statistics import median

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
a = [i for i, j in ab]
b = [j for i, j in ab]

if n % 2 == 1:
    print(abs(median(b) - median(a)) + 1)
else:
    print(int(abs(median(b) - median(a)) * 2) + 1)