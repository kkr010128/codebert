n = int(input())
k = list(map(int, input().split()))
m = 1000
s = 0
for i in range(n - 1):
    if k[i + 1] > k[i]:
        s = m // k[i]
        m += s * (k[i + 1] - k[i])
print(m)
