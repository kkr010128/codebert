n, a, b = map(int, input().split())
if (a+b) % 2 == 0:
  print((b-a)//2)
else:
  if b == a + 1:
    print(min(b-1, n-a))
  else:
    cnt_1 = a + (b-a-1)//2
    cnt_n = n - b + 1 + (b-a-1)//2
    print(min(cnt_1, cnt_n))
