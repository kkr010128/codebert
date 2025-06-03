A,B,C = map(int,input().split())
if A == B and B == C and C == A:
  ans = "No"
elif A == B or B == C or C == A:
  ans = "Yes"
else:
  ans = "No"
  
print(ans)