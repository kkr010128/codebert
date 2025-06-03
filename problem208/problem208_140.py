def lstToInt(l,x=0):
  if len(l) == 0:
    return x
  else:
    return lstToInt(l[1:], x*10 + l[0])

n,m = map(int,input().split())
c = [-1]*n

for i in range(m):
  s, num = map(int,input().split())
  if c[s-1] != -1 and c[s-1] != num:
    print(-1)
    exit()
  elif s == 1 and num == 0 and n != 1:
    print(-1)
    exit()
  else:
    c[s-1] = num

if c[0] == -1 and n != 1:
  c[0] = 1

ans = lstToInt(list(0 if c[i] == -1 else c[i] for i in range(n)))
print(ans)