D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]
out = [int(input()) for _ in range(D)]

sat = 0
last = [0] * 26
for d in range(D):
    assert(1 <= out[d] and out[d] <= 26)
    j = out[d] - 1
    last[j] = d + 1
    for i in range(26):
        sat -= (d + 1 - last[i]) * c[i]
    sat += s[d][j]
    print(sat)