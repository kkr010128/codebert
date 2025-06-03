A,B,K = map(int, input().split())
if A+B<=K:
     print(0,0)
elif A>=K:
     A=A-K
     print(A,B)
else:
     B=B-(K-A)
     print(0,B)
