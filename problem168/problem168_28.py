N,M = map(int,input().split())
home = list(map(int,input().split()))

if N - sum(home) < 0:
    print("-1")
else:
    print(N - sum(home))