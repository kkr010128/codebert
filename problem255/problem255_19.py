N = int(input())
s,t = map(str,input().split())
ans = list()
for i in range(N):
  ans.append(s[i])
  ans.append(t[i])
  
for i in range(N*2):
  print(ans[i],end='')