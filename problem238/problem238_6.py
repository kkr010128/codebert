n, k, s = list(map(int, input().split()))

ans = []

for i in range(k):
    ans.append(s)

alt = s+1 if s < 1e9 else s-1
for i in range(n-k):
    ans.append(alt)

print(" ".join(map(str, ans)))