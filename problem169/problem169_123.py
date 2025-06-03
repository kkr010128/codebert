n = int(input())
d = dict(zip([i for i in range(1, n + 1)], [0] * n))
l = map(int, input().split())
for i in l:
    d[i] += 1
for i in d.values():
    print(i)