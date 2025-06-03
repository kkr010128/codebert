A,B=map(int,input().split())
if B < A:
  A,B=B,A
for i in range(B):
 print(A, end="")
print()