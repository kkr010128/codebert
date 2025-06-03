S,T=map(str, input().split())
A,B=map(int,input().split())
U=input()

if S==U:
  a=1
  b=0
else:
  a=0
  b=1

print(A-a,B-b)