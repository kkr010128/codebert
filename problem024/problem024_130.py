import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15


N,K = map(int,input().split())
W = [int(input()) for _ in range(N)]

r = 10 ** 10
l = 0
def ok(x):
    cnt = 1
    tot = 0
    for i in range(N):
        if tot + W[i] <= x:
            tot += W[i]
        else:
            cnt += 1
            if W[i] > x:
                return False
            tot = W[i]
    return cnt <= K      

while r - l > 1:
    mid = (r + l)//2
    if ok(mid):
        r = mid
    else:
        l = mid
print(r)

