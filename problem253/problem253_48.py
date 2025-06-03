N, A, B=map(int, input().split())
if (B-A)%2==0:
  print((B-A)//2)
else:
  if A==1 or B==N:
    ans=(B-A-1)//2+1
  else:
    ans=min(A-1, N-B)+(B-A-1)//2+1
  print(ans)
