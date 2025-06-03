n=int(input())
s=input()
ans=""
alp=[i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
for i in s:
  ind=alp.index(i)
  ind+=n
  if 25<ind:
    ind=ind-26
  ans+=alp[ind]
print(ans)