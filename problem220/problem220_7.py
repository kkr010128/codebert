S,U = map(str,input().split())
M,N = map(int,input().split())
a = str(input())
if S == a:
  print(M-1,N)
else:
  print(M,N-1)