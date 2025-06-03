n,k = map(int, input().split())
h = list(map(int, input().split()))
nk = [h for h in h if h >= k]
print(len(nk))