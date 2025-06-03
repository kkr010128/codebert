h1,m1,h2,m2,K = map(int,input().split() )

H=h2-h1
M=m2-m1

if(M<0):
  M += 60
  H -= 1
if(H<0):
  H += 24

M += H*60

ans =M - K
print(ans)