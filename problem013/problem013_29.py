
n = int(input())

R = []

for i in range(n):
    R.append(int(input()))

minv = R[0]
maxv = R[1] - R[0]

for r in R[1:]:
    maxv = max(maxv, r - minv)
    minv = min(minv, r)

print(maxv)