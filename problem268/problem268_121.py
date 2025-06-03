n = int(input())
a = list(map(int, input().split()))
que = [-1, -1, -1]
ans = 1
for i in range(n):
  if que[0]+1 == a[i]:
    if que[0] == que[1] and que[0] == que[2]:
      ans *= 3
      ans %= (10**9 + 7)
    elif que[0] == que[1]:
      ans *= 2
      ans %= (10**9 + 7)
    que[0] = a[i]
  elif que[1]+1 == a[i]:
    if que[1] == que[2]:
      ans *= 2
      ans %= (10**9 + 7)
    que[1] = a[i]
  elif que[2]+1 == a[i]:
    que[2] = a[i]
  else:
    ans = 0
    break
print(ans)
