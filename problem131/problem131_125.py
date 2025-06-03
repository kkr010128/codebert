import sys
input = sys.stdin.readline
P = [list(map(int,input().split())) for i in range(2)]
T = int(input())
if(P[0][1]<P[1][1]):
  print('NO')
else:
  if(abs(P[0][0]-P[1][0])<=abs(P[0][1]-P[1][1])*T):
    print('YES')
  else:
    print('NO')