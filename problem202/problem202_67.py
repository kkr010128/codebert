N,A,B = map(int,input().split())
amari = N % ( A+B )
rep = N // ( A+B )
if amari >= A:
  count = A
else:
  count = amari
ans = rep*A + count
print(ans)
