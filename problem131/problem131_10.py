A,V = map(int,input().split())
B,W = map(int,input().split())
 
T = int(input())

D1 = abs(A-B)
D2 = (V-W)*T

if (D1 - D2) <=0:
  print("YES")
else:
  print("NO")
