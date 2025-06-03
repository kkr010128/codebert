n = int(input())
P = list(map(int, input().split( )))
mas = P[0]
ans = 1
for i in range(n-1):
  if mas >= P[i+1]:
    ans += 1
  mas = min(mas,P[i+1])

print(ans)