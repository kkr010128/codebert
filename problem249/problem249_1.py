A,B,K = list(map(int,input().split()))
if A>= K:
    print(str(A-K) + ' ' + str(B))
elif A < K :
    print(str(0) + ' ' + str(max(B+A-K,0)))
