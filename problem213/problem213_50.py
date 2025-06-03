N = int(input())
X = list(map(int, input().split()))
X.sort()
ans = 0
data = []

for p in range(X[N-1] + 1):
    sum = 0
    for i in range(len(X)):
         sum += (X[i]-p)**2
         ans = sum
    p += 1
    data.append(ans)

print(min(data))
