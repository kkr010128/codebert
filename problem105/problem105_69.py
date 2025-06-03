n = int(input())
arr = [int(x) for x in input().split()]
ans = 0
for i in range(n):
  ans += (i+1)%2 and arr[i]%2
print(ans)