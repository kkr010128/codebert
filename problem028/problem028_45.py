n,m = map(int,input().split())
c = list(map(int,input().split()))

minimum = [50000] * (n+1)
minimum[0] = 0

for i in range(1,n+1):
    for j in range(m):
        if c[j]<=i and minimum[i-c[j]] + 1 < minimum[i]:
            minimum[i] = minimum[i-c[j]]+1

print(minimum[n])