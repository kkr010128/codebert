A,V=map(int,input().split())
B,W=map(int,input().split())
T=int(input())
if(A<B):
  A1=A+V*T
  B1=B+W*T

  if(A1>=B1):
    print('YES')
  else:
    print('NO')
    
else:
  A1=A-V*T
  B1=B-W*T

  if(A1<=B1):
    print('YES')
  else:
    print('NO')