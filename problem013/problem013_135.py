n = int(input())
minv = int(input())
maxv = (10**9)*(-1)
for j in range(1,n):
    r = int(input())
    if maxv < (r - minv):
        maxv = r - minv
    if minv > r:
        minv = r
print(maxv)