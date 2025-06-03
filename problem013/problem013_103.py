n = int(input())
R = [int(input()) for i in range(n)]

minv = float('inf')
maxv = -float('inf')
for r in R:
    maxv = max(maxv, r-minv)
    minv = min(minv, r)
print(maxv)