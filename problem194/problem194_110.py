from collections import deque
h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]
DP = [[10000]*w for _ in range(h)]
DP[0][0] = 0 if S[0][0]=='.' else 1

directs = [[0,1], [1,0]]
for hi in range(h):
    for wi in range(w):
        for dh,dw in directs:
            if not (0<=hi+dh<h and 0<=wi+dw<w): continue
            if S[hi][wi]=='.' and S[hi+dh][wi+dw]=='#':
                DP[hi+dh][wi+dw] = min(DP[hi+dh][wi+dw], DP[hi][wi]+1)
            else:
                DP[hi+dh][wi+dw] = min(DP[hi+dh][wi+dw], DP[hi][wi])
print(DP[-1][-1])