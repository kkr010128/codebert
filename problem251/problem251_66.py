n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=input()

point = 0
flg=[0]*n
for i in range(n):
  if t[i] == 'r' and flg[i] == 0:
    point += p
  elif t[i] == 's' and flg[i] == 0:
    point += r
  elif t[i] == 'p' and flg[i] == 0:
    point += s

  if i+k < n and t[i+k] == t[i]:
    if t[i] == 'r' and flg[i] == 0:
      flg[i+k] = 'r'
    elif t[i] == 's' and flg[i] == 0:
      flg[i+k] = 's'
    elif t[i] =='p' and flg[i] == 0:
      flg[i+k] = 'p'
print(point)