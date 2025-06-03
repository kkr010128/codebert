import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())
K = int(input())
leng = len(S)
if len(set(S))==1:
    print(K*leng//2)
    exit()
if S[0]!=S[-1] or K==1:
    last = S[0]
    cnt = 0
    for s in S[1:]:
        if s==last:
            cnt += 1
            last = '.'
        else:
            last = s
    print(cnt*K)
else:
    S += ['.']
    cnt = 1
    lis = []
    last = S[0]
    for s in S[1:]:
        if s==last:
            cnt += 1
        else:
            lis.append(cnt)
            last = s
            cnt = 1
    first = lis.pop(0)
    end = lis.pop()
    others = sum([i//2 for i in lis])
    ans = first//2 + others*K + (first+end)//2*(K-1)+end//2
    print(ans)
