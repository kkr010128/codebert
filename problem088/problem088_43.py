n=int(input())
a = list(map(int, input().split()))
ans = 0
temp = a[0]
for i in a[1:]:
  if temp > i:
    ans += (temp - i)
  temp = max(temp, i)
  
print(ans)