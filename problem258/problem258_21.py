N = int(input())

ans = 0
if N % 2 == 0:
  ans += N//10
  ans += N//50
  N //= 50
  while N > 0:
    N //= 5
    ans += N
print(ans)