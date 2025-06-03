A,B,C = map(int,input().split())
ans = "No"
if A == B and A != C:
  ans = "Yes"
elif B == C and B != A:
  ans = "Yes"
elif C == A and C != B:
  ans = "Yes"
print(ans)