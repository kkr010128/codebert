n = int(input())
a = sorted([(i, int(ai)) for i, ai in zip(range(1, n + 1), input().split())], key=lambda x: x[1])
for i in range(n):
    print(a[i][0], end=' ')