A,B,C,K = map(int,input().split())

ans = 0
if K > A:
  ans += A
  K -= A
  if K > B:
    ans += 0
    K -= B
    if K > 0:
      ans -= K
  else:
    ans += 0
else:
  ans = K
  
print(ans)