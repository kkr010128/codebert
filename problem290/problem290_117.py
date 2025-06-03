
#test

N,K = map(int,input().split())
A = list(map(int,input().split()))
F = list(map(int,input().split()))

A.sort()
F.sort(reverse=True)
AF = [A[i]*F[i] for i in range(N)]

l = -1
r = max(AF)

while r-l > 1:
    x = (l+r)//2
    k =0
    #スコアをx以下にするのに必要な最小コストを算出
    for i in range(N):
        if AF[i]<=x:
            continue
        else:
            k += A[i]-x//F[i]
    if k <= K:
        r = x
    else:
        l=x

print(r)