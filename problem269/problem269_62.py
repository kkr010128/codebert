t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

if (a1 > b1 and a2 > b2) or (a1 < b1 and a2 < b2):
  print(0)
else:
  if a1 * t1 + a2 * t2 == b1 * t1 + b2 * t2:
    print("infinity")
  else:
    d_all = (a1 * t1 + a2 * t2) - (b1 * t1 + b2 * t2)
    d_1 = a1 * t1 - b1 * t1
    if (d_all > 0 and d_1 > 0) or (d_all < 0 and d_1 < 0):
      print(0)
    else:
      if abs(d_all) > abs(d_1):
        print(1)
      else:
        ans = 1
        ans += abs(d_1) // abs(d_all) * 2 - (1 if d_1 % d_all == 0 else 0)
        print(ans)