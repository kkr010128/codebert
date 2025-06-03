
from collections import defaultdict

N, P = map(int, input().split())
S = input()

if P == 2 or P == 5:
    ans = 0
    for i in range(N):
        if int(S[i]) % P == 0:
            ans += i + 1
    print(ans)
else:
    ctr = defaultdict(int)
    ctr[0] = 1
    cur = 0
    for i in reversed(range(N)):
        cur = (cur + int(S[i]) * pow(10, N - i - 1, P)) % P
        ctr[cur] += 1

    ans = 0
    for v in ctr.values():
        ans += v * (v - 1) // 2
    print(ans)
