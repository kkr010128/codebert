count, outrate = map(int, input().split())

if count >= 10:
  result = outrate
  print(result)
else:
  result = outrate + 100 * (10 - count)
  print(result)
