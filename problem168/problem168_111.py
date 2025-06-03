N,M = map(int,input().split())
A = [int(x) for x in input().split()]

if N - sum(A) >= 0 :
    print(N-sum(A))
else :
    print("-1")