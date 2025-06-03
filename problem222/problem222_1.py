N=int(input())
A=input().split()
S={}
for a in A:
  if a in S.keys():
    print('NO')
    break
  S[a]=1
else:
  print('YES')