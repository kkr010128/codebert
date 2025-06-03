k = int(input())

if k % 2 == 0 or k % 5 == 0:
  print(-1)
else:
  ans = 7
  cnt = 1
  while 1:
    if ans % k == 0:
      break
    else:
      cnt += 1
      ans *= 10
      ans += 7
      ans %= k

  print(cnt)      
