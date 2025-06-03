N = int(input())
A = tuple(map(int, input().split()))

dupcount = [0] * (N + 1)
for a in A:
    dupcount[a] += 1

allc = 0
for a in range(1, N + 1):
    c = dupcount[a]
    if c > 1:
        allc += (c * (c - 1) // 2)

for a in A:
    ans = allc
    c = dupcount[a]
    if c > 0:
        ans -= (c - 1)
    print(ans)