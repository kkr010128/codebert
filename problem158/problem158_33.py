k = int(input())
a,b = [int(x) for x in input().split()]
ans = "NG"
for i in range(1000):
  if a <= i * k and i * k <= b:
    ans = "OK"
    break
print(ans)