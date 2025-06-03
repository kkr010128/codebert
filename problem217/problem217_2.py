n = int(input())
a = map(int,input().split())
ans = "APPROVED"

for i in a:
  if i%2 == 0:
    if not(i%3==0 or i%5==0):
      ans = "DENIED"

print(ans)