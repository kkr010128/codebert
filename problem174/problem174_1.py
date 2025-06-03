import itertools
k = int(input())

d = [[] for _ in range(k)]

for i in range(1, k+1):
    n = 1
    while i*n <= k:
        d[i*n-1].append(i)
        n += 1

seq = [i for i in range(1, k+1)]
ans = 0
A = list(itertools.combinations_with_replacement(seq, 3))
for a in A:
    a1 = a[0]
    a2 = a[1]
    a3 = a[2]
    if a1 == a2 == a3:
        m = 1
    elif a1 == a2 or a1 == a3 or a2 == a3:
        m = 3
    else:
        m = 6
    ans += max(set(d[a1-1]) & set(d[a2-1]) & set(d[a3-1])) * m

print(ans)