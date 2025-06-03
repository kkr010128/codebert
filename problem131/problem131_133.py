def solve(d,p,t):
  if d - p * t <= 0:
    return "YES"
  else:
    return "NO"

A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())

d = abs(B-A)
p = V - W
print(solve(d,p,T))