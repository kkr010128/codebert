N, M = map(int, input().split())
a = 1
b = N
d = set([1, N - 1])
for _ in range(M):
    print(a, b)
    a += 1
    b -= 1
    while (b - a) in d or (N - b + a) in d or (b - a) == (N - b + a): b -= 1
    d.add(b - a)
    d.add(N - b + a)
