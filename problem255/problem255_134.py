n = int(input())
a , b = input().split()
ans = ""
for i in range(n):
  ans += a[i]
  ans += b[i]
print(ans)
