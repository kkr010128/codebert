N,K = map(int,input().split())
hitpoint = list(map(int,input().split()))
hitpoint.sort(reverse=True)
if N<=K:
    print(0)
else:
    print(sum(hitpoint[K:]))