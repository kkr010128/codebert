N,A,B = map(int,input().split())

dif = abs(A-B)
if(dif%2 == 0):
  ans = dif//2
else:
  A1_diff = A-1
  #B1_diff = B-1
  #AN_diff = N-A
  BN_diff = N-B
  ans = min(A1_diff, BN_diff)+1+(dif-1)//2
print(ans)  