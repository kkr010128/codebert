"""
タグ：区間
"""
import sys
input = sys.stdin.readline
N, P = map(int, input().split())
S = input().strip()

if P == 5:
    res = 0
    i = 0
    for s in reversed(S):
        if int(s)%5==0:
            res += N-i
        i += 1
    print(res)
elif P == 2:
    res = 0
    i = 0
    for s in reversed(S):
        if int(s)%2==0:
            res += N-i
        i += 1
    print(res)
else:
    T = [0]
    p = 1
    for s in reversed(S):
        T.append(int(s)*p + T[-1])
        p = p*10%P

    cnt = [0]*P
    for i in range(N+1):
        cnt[T[i]%P] += 1

    res = 0
    for c in cnt:
        res += c*(c-1)//2
    print(res)