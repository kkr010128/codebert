def scoring(d, t):
    arr = [l for l in last]
    arr[t] = d
    return S[d][t] - sum((d - l) * c for l, c in zip(arr, C))

D = int(input())
C = list(map(int, input().split()))
S = []
for _ in range(D):
    s = list(map(int, input().split()))
    S.append(s)
last = [-1] * 26
ans = []
for i in range(D):
    res = -10 ** 6
    idx = -1
    for j in range(26):
        tmp = scoring(i, j)
        if tmp > res:
            res = tmp
            idx = j
    last[idx] = i
    ans.append(idx+1)
print(*ans, sep='\n')