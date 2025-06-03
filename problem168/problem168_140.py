N,M=map(int,input().split())
a = list(map(int,input().split()))
if N-sum(a)>=0:
    print(N-sum(a))
else:
    print("-1")