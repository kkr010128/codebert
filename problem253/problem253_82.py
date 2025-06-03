N,A,B=map(int,input().split())
ans=0
 
if (B-A)%2==0:
  ans=(B-A)//2
else:
  if A-1<N-B:
    if B-A==1:
      ans=B-1
    else:
      ans=A+(B-A-1)//2
  else:
    if B-A==1:
      ans=N-A
    else:
      ans=N-B+1+(N-(A+N-B+1))//2
print(ans)