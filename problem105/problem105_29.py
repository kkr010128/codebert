n = int(input())
a = list(map(int, input().split()))

assert(len(a) == n)

ans = 0
for i in range(n):
  if not i % 2 and a[i] % 2:
    ans += 1
    
print(ans)
