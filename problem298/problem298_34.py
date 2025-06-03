n,k = map(int,input().split())
h = list(map(int,input().split()))
print(sum(h[i] >= k for i in range(n)))
