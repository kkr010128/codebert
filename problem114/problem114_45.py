d = int(input())
c = list(map(int,input().split()))
s = []
for i in range(d):
  si = list(map(int,input().split()))
  s.append(si)
lastd = [-1 for _ in range(26)]
ans = 0
for i in range(d):
  di = int(input())
  lastd[di-1] = i
  ans += s[i][di-1]
  for j in range(26):
    ans -= (i-lastd[j])*c[j]
  print(ans)