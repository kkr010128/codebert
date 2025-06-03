h, a = map(int, input().split())
if h % a > 0:
  number_of_times = h // a + 1
  print(number_of_times)
else:
  print(h // a)