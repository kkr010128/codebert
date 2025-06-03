A,B,K = map(int,input().split())

a = A-K
if a < 0:
  A = 0
  B = max(0, B+a)

print(max(0,a), B)