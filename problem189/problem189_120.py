N,M=map(int,input().split())
ans=0
if N>1:
  ans += N*(N-1)//2
else:
  pass
if M>1:
  ans += M*(M-1)//2
else:
  pass
print(ans)