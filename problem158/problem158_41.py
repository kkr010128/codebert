n = int(input())
lim_min, lim_max = map(int, input().split())

if lim_min % n == 0 :
  print('OK')
elif lim_min + n - (lim_min % n) <= lim_max:
  print('OK')
else:
  print('NG')
