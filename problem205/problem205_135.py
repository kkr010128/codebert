import sys
input = sys.stdin.readline
from collections import *

N, P = map(int, input().split())
S = input()[:-1]

if P in [2, 5]:
    ans = 0
    
    for i in range(N):
        if int(S[i])%P==0:
            ans += i+1
    
    print(ans)
    exit()

cnt = defaultdict(int)
cnt[0] = 1
now = 0
ans = 0

for i in range(N-1, -1, -1):
    now = (int(S[i])*pow(10, N-1-i, P)+now)%P
    ans += cnt[now]
    cnt[now] += 1

print(ans)