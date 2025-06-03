N, A, B = [int(x) for x in input().split()]
n = N//(A+B)
ans = n * A
d = N - n*(A+B)
if d >= A:
  ans += A
else:
  ans += d
print(ans)