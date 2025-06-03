N,A,B = map(int,input().split())
if A%2 != 0 and B%2 == 0:
  ans = (B-A-1)//2 + min(A-1,N-B) + 1
elif A%2 == 0 and B%2 != 0:
  ans = (B-A-1)//2 + min(A-1,N-B) + 1
else:
  ans = (B-A)//2
print(ans)