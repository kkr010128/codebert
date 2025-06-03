n, m = map(int, input().split())
s = input()
s = s[::-1]
loc = 0
anslist=[]
while True:
  if loc >= n-m:
    anslist.append(n-loc)
    break
    quit()
  next = m
  while s[loc+next]=="1":
    next-=1
    if next == 0:
      print(-1)
      quit()
  anslist.append(next)
  loc+=next
ans=anslist[::-1]
ans = list(map(str, ans))
print(" ".join(ans))