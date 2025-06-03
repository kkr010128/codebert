N,M=map(int,input().split())
ans=['0']*N
I=[]
for _ in range(M):
  s,c=input().split()
  index=int(s)-1
  if index==0 and N>1 and c=='0':
    print(-1)
    break
  if index in I and ans[index]!=c:
    print(-1)
    break
  ans[index]=c
  I.append(index)
else:
  if 0 not in I and N>1:
    ans[0]='1'
  print(''.join(ans))