n = int(input())
a = list(map(int,input().split()))
mod = 1000000007
ans = 1
l = []
for i in range(n):
  if a[i] == 0:
    l.append(0)
    ans = ans*(4-len(l))%mod
  else:
    id = -1
    count = 0
    for j in range(len(l)):
      if l[j] == a[i] - 1:
        count += 1
        id = j
    if id == -1:
      ans = 0
      break
    ans = (ans*count)%mod
    l[id] = a[i]
  if ans == 0:
    break
print(ans%mod)