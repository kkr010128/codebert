A, B, C, K = map(int, input().split())

ans = 0
if A > K:
  ans += 1*K
else:
  ans += 1*A
  K = K - A
  if B > K: 
    ans += 0*K
  else:
    ans += 0*B
    K = K - B
    if C > K:
      ans += -1*K
    else:
      ans += -1*C

print(ans)

