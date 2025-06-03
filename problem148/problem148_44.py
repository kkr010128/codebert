A,B,C,K = map(int,input().split())
if K<=A:
  Ans = K
elif K<=A+B:
  Ans = A
elif K<=A+B+C:
  Ans = A-(K-A-B)
else:
  Ans = A-C

print(Ans)
