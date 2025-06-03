A,B,C=map(int,input().split())
K=int(input())
ans="No"
for _ in range(K+1):
  if A>=B:
    B*=2
  elif B>=C:
    C*=2
  else:
    ans="Yes"
print(ans)
