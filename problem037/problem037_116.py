time = int(input())
if time != 0:
  h = time // 3600
  time = time % 3600
  m = time // 60
  s = time % 60
  print(str(h) + ':' + str(m) + ':' + str(s))
else:
  print('0:0:0')