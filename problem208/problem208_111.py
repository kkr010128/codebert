N,M = map(int,input().split())
ans = [-1]*N
flg = 0
 
for i in range(M):
  s,c = map(int, input().split())
  s -= 1
  if ans[s] == -1 or ans[s] == c:
    ans[s] = c
  else:
    flg = 1
  
if flg == 0:
  if N == 1 and ans[0] == -1 or N == 1 and ans[0] == 0:
    print("0")
  elif ans[0] == 0:
    print("-1")
  else:
    if ans[0] == -1:
      ans[0] = 1
    for i in range(1,N):
      if ans[i] == -1:
        ans[i] = 0
    print(int("".join(map(str,ans))))
else:
  print("-1")