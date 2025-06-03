n,k = map(int,input().split())
h = list(map(int,input().split()))
h = sorted(h,reverse = True)

h1 = h[k:n]
print(sum(h1))