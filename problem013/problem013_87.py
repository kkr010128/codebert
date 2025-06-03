N = input()
a = [input() for i in range(N)]

maxv = a[-1] - a[0]
minv = a[0]

for i in range(1,N):
    maxv = max(maxv,a[i]-minv)
    minv = min(minv,a[i])

print maxv