n = int(input())
R = []
for _ in range(n):
    R.append(int(input()))

maxv = R[1] - R[0]
minv = R[0]
for j in range(1, n):
    maxv = max(R[j] - minv, maxv)
    minv = min(R[j],minv)
print(maxv)