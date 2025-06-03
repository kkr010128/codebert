N, M = map(int, input().split())
A = list(map(int, input().split()))
cr = sum(A) / (4*M)
Arev = sorted(A, reverse = True)

if Arev[M-1] >= cr:
    print('Yes')
else:
    print('No')