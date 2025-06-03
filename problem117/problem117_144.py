n,m,k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_c_sum = [0]*(n + 1)
for i in range(n):
  a_c_sum[i + 1] = a_c_sum[i] + a[i]
b_c_sum = [0]*(m + 1)
for i in range(m):
  b_c_sum[i + 1] = b_c_sum[i] + b[i]

ans, best_b = 0, m
for i in range(n + 1):
  if a_c_sum[i] > k:
    break
  else:
    while 1:
      if b_c_sum[best_b] + a_c_sum[i] <= k:
        ans = max(ans, i + best_b)
        break
      else:
        best_b -= 1
        if best_b == 0:
          break
print(ans)