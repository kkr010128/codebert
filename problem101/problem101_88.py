A, B, C = list(map(int, input().split()))
K = int(input())
while(B <= A):
  B *= 2
  K -= 1
while(C <= B):
  C *= 2
  K -= 1
if(K >= 0): print("Yes")
else: print("No")