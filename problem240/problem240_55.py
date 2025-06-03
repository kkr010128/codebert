N, M = map(int, input().split())
a = [False] * N
w = [0] * N
for i in range(M):
    p, S = input().split()
    if S == 'AC':
        a[int(p)-1] = True
    elif not a[int(p)-1]:
        w[int(p)-1] += 1
print(a.count(True), sum([w[i] if a[i] else 0 for i in range(N)]))
