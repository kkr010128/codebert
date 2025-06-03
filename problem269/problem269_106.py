ma = lambda: map(int, input().split())
t,u = ma(); a,c = ma(); b,d = ma()
p = (a-b)*t; q = (c-d)*u
if p < 0: p *= -1; q *= -1
if p+q > 0: print(0)
elif p+q == 0: print('infinity')
else:
  t = -p-q
  print(1+(p//t)*2 if p%t else (p//t)*2)