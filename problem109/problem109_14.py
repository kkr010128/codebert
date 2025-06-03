N=input()
n=int(N)
a=0
w=0
t=0
r=0
for j in range(n):
  c=input()
  if c=='AC':
    a+=1
  elif c=='WA':
    w+=1
  elif c=='TLE':
    t+=1
  elif c=='RE':
    r+=1
print('AC x {}'.format(a))
print('WA x {}'.format(w))
print('TLE x {}'.format(t))
print('RE x {}'.format(r))
