N = int(input())
X = [int(i) for i in input().split()]

a = min(X)
b = max(X)

s = 10**6
for i in range(a, b+1):
    t = 0
    for j in range(N):
        t += (X[j] - i)**2
    if t < s:
        s = t

print(s)