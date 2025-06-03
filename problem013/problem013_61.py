n = int(input())

maxv = -20000000000

minv = int(input())

for i in range(n-1):
    R = int(input())
    maxv = max(maxv, R - minv)
    minv = min(minv, R)

print(maxv)