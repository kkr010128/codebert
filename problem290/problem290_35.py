N, K  = map(int, input().split())
A = list(map(int, input().split()))
F = list( map(int, input().split()))
A.sort()
F.sort(reverse=True)

la = 10**12+1
sm = -1
while sm+1<la:
    mi = (sm+la)//2
    y=0
    for i in range(N):
        y += max(0, A[i]-(mi//F[i]))
    if y<=K:
        la = mi
    else:
        sm = mi
print(la)