from collections import defaultdict

N, P = map(int, input().split())
S = input()
if P == 2 or P == 5:
    ans = 0
    for i in range(N):
        d = int(S[i])
        if d % P == 0:
            ans += i + 1
    print(ans)
else:
    ans = 0
    count = defaultdict(int)
    count[0] = 1
    num = 0
    factor = 1
    for i in range(N)[::-1]:
        num = (num + int(S[i]) * factor) % P
        factor = factor * 10 % P
        ans += count[num]
        count[num] += 1
    print(ans)
