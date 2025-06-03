n = int(input())
l = list(map(int, input().split()))

ans = 0
for i in range(n):
  for ii in range(i+1, n):
    ans += l[i]*l[ii]

print(ans)