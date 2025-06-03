n = int(input())

ans = 0
for i in range(1, n+1):
  if i*2 > n:
    # 一気に足し上げて抜ける
    ans += (i + n) * (n - i + 1) // 2
    break

  # n 以下の最大の i の倍数
  last_term = n // i * i
  num_term = (last_term - i) // i + 1
  ans += (i + last_term) * num_term // 2
   

print(ans)
