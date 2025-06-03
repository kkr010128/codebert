N,M=map(int,input().split())
S=input()
ans=''
i=N
flg=0
while i>0:
  j=M
  if i-M<0:
    ans=str(i)+' '+ans
    i=0
  else:
    while j>=0:
      if j>0 and S[i-j] == '0':
        ans=str(j)+' '+ans
        i-=j
        j=0
      elif j==0:
        flg=1
        i=0
      j-=1
if flg==1:
  print(-1)
else:
  print(ans)