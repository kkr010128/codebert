n = int(input())
table = [0] * (n + 1)

for i in range(1, n+1):
  for j in range(i, n+1, i):
    table[j] += 1

ans = 0
for i in range(n+1):
  ans += table[i] * i
print(ans)
