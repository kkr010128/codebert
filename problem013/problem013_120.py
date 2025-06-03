n = int(input())
minv = int(input())
maxv = -2*10**9
for i in range(n-1):
    r = int(input())
    maxv = max(maxv,r-minv)
    minv = min(minv,r)
print(maxv)