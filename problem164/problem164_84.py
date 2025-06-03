t_p, t_a, a_p, a_a = map(int, input().split())

while True:
  a_p -= t_a
  if a_p <= 0 :
    print('Yes')
    exit()
  
  t_p -= a_a
  if t_p <= 0 :
    print('No')
    exit()
